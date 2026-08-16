#!/usr/bin/env python3
"""Refuse a public-site publication when its routes or source tree are unsafe."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
from urllib.parse import unquote, urlsplit


DEPLOYABLE_NAMES = {"CNAME", "vercel.json", ".vercelignore"}
DEPLOYABLE_SUFFIXES = {".css", ".html", ".js", ".mjs"}
SKIPPED_SCHEMES = {"data", "javascript", "mailto", "tel"}


class HrefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        for name, value in attrs:
            if name.lower() == "href" and value:
                self.hrefs.append(value)


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=root, text=True, capture_output=True, check=False
    )


def is_deployable(relative_path: str) -> bool:
    path = Path(relative_path)
    return path.name in DEPLOYABLE_NAMES or path.suffix.lower() in DEPLOYABLE_SUFFIXES


def deployable_status_errors(root: Path) -> list[str]:
    result = git(root, "status", "--porcelain", "--untracked-files=all", "-z")
    if result.returncode:
        return ["could not inspect Git working tree"]

    errors: list[str] = []
    entries = iter(result.stdout.split("\0"))
    for entry in entries:
        if not entry:
            continue
        status, relative_path = entry[:2], entry[3:]
        if status[0] in {"R", "C"}:
            next(entries, None)
        if not is_deployable(relative_path):
            continue
        if status == "??":
            errors.append(f"untracked deployable source: {relative_path}")
        else:
            errors.append(f"modified deployable source: {relative_path}")
    return errors


def tracked_html_files(root: Path) -> list[Path]:
    result = git(root, "ls-files", "-z", "--", "*.html")
    if result.returncode:
        return []
    return [root / value for value in result.stdout.split("\0") if value]


def route_target(root: Path, href: str) -> Path | None:
    parts = urlsplit(href)
    if parts.scheme.lower() in SKIPPED_SCHEMES or parts.scheme or parts.netloc:
        return None
    if not parts.path.startswith("/"):
        return None
    route = unquote(parts.path).lstrip("/")
    candidates = [Path("index.html")] if not route else []
    if route:
        requested = Path(route)
        if requested.suffix:
            candidates.append(requested)
        else:
            candidates.extend([Path(f"{route}.html"), requested / "index.html"])
    for candidate in candidates:
        target = (root / candidate).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            continue
        if target.exists():
            return target
    return (root / candidates[0]).resolve() if candidates else None


def link_errors(root: Path) -> list[str]:
    errors: list[str] = []
    for source in tracked_html_files(root):
        parser = HrefParser()
        parser.feed(source.read_text(encoding="utf-8", errors="replace"))
        source_name = source.relative_to(root).as_posix()
        for href in parser.hrefs:
            target = route_target(root, href)
            if target is None:
                continue
            try:
                target_name = target.relative_to(root.resolve()).as_posix()
            except ValueError:
                errors.append(f"{source_name} links outside site root: {href}")
                continue
            if not target.exists():
                errors.append(f"{source_name} links to missing target: {target_name}")
            elif git(root, "ls-files", "--error-unmatch", "--", target_name).returncode:
                errors.append(f"{source_name} links to untracked target: {target_name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()

    errors = deployable_status_errors(root) + link_errors(root)
    if errors:
        for error in errors:
            print(f"site validation: {error}", file=sys.stderr)
        return 1
    print("site validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

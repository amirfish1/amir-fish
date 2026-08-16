"""Regression tests for the public-site publication validator."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_site.py"


class SiteValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.site = Path(self.temp_dir.name) / "site"
        self.site.mkdir()
        self._git("init", "-q")
        self._git("config", "user.email", "test@example.invalid")
        self._git("config", "user.name", "Validator Test")
        self.write("index.html", '<a href="/about">About</a>')
        self.write("about.html", "<h1>About</h1>")
        self._commit("initial site")

    def tearDown(self):
        self.temp_dir.cleanup()

    def _git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.site, check=True, capture_output=True, text=True
        )

    def _commit(self, message):
        self._git("add", ".")
        self._git("commit", "-qm", message)

    def write(self, relative_path, contents):
        target = self.site / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(contents, encoding="utf-8")

    def validate(self):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(self.site)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_accepts_committed_local_page_links(self):
        result = self.validate()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_local_link_to_an_untracked_page(self):
        self.write("index.html", '<a href="/draft">Draft</a>')
        self._commit("link draft")
        self.write("draft.html", "<h1>Draft</h1>")

        result = self.validate()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("untracked target: draft.html", result.stderr)

    def test_rejects_modified_deployable_source(self):
        self.write("styles.css", "body { color: black; }\n")
        self._commit("add stylesheet")
        self.write("styles.css", "body { color: navy; }\n")

        result = self.validate()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("modified deployable source: styles.css", result.stderr)

    def test_rejects_untracked_deployable_source(self):
        self.write("draft.html", "<h1>Draft</h1>")

        result = self.validate()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("untracked deployable source: draft.html", result.stderr)


if __name__ == "__main__":
    unittest.main()

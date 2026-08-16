#!/usr/bin/env bash
# Publish only a reviewed, validated AmirFish public-site revision.
set -euo pipefail

SITE_URL="${AMIRFISH_SITE_URL:-https://amirfish.ai}"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --site-url) SITE_URL="${2:-}"; shift 2 ;;
    --site-url=*) SITE_URL="${1#*=}"; shift ;;
    -*) echo "publish-site: unknown flag $1" >&2; exit 2 ;;
    *) echo "publish-site: unexpected argument $1" >&2; exit 2 ;;
  esac
done

[ -n "$SITE_URL" ] || { echo "publish-site: site URL must not be empty" >&2; exit 2; }
git rev-parse --is-inside-work-tree >/dev/null

python3 scripts/validate_site.py
git fetch origin main
read -r BEHIND AHEAD <<<"$(git rev-list --left-right --count origin/main...HEAD)"
if [ "$BEHIND" -ne 0 ]; then
  echo "publish-site: local main is behind origin/main; rebase or merge before publishing" >&2
  exit 1
fi

git push origin main
vercel --prod --yes
curl --fail --silent --show-error --max-time 20 "$SITE_URL" > /dev/null
echo "publish-site: deployed and verified ${SITE_URL}"

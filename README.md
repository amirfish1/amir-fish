# amir-fish
Personal website for amirfish.ai

## Publish

Run `scripts/publish_site.sh` from a clean, reviewed site revision. It checks
local page links and deployable source files, pushes `main`, deploys to Vercel,
and verifies `https://amirfish.ai`. It never stages or commits local files.

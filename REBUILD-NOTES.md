# Rebuild Notes — May 4–5, 2026

Context: ground-up refresh of amirfish.ai to match the typeset voice already established in `index.html` and `parallel-sessions.html`. Built autonomously while Amir was AFK.

## Voice / design decisions

- **Kept:** Embedded `<style>` per page. DM Sans + Fraunces. 650px container. "Field Note" tag. The `.ccc-card` block from `parallel-sessions.html`. No build step, no framework.
- **Rejected:** The older `styles.css` + nav bar + `btn-primary` salesy stack. Per CLAUDE.md it's being phased out — no point extending it.
- **Tone bar:** Reads like a builder writing for other builders. No "I help AI startups get to product-market fit faster." No marketing punch lines. No exclamation. Numbered insights only when the post earns them.

## Page-by-page decisions

### `index.html` (homepage)
- Refreshed Field Notes list to **link** to per-note pages (previously just static cards).
- Added a new Field Note for the NVIDIA workshop / PM Operating System thesis ("The Spec Is the Hard Part") — pulled from `~/Workshops/Claude_workshop/Post/V8.5_linkedin_post.md` and `V6_linkedin_post.md` because that material has been Amir's strongest recent output and was missing from the homepage.
- Added a CCC banner above the Building section. The site previously had zero CCC promo on the homepage despite CCC being one of the three conversion goals.
- Building section: kept Kneaded.ai, plts.xyz, Finance Tools. Added CCC as its own item (it deserves a line, not just a banner).
- Advisory CTA: kept the email-based path. Did not invent a Calendly link or pricing — Amir hasn't published those in the typeset voice and the briefing said no questions during run.

### Per-Field-Note pages (new)
All five use the `parallel-sessions.html` structural template:

1. **`/guided-verification.html`** — The Guided Verification Problem. The expense-tracker UX story. The strongest IP on the site.
2. **`/small-business-cofounder.html`** — Every Small Business Deserves a Technical Co-Founder. The Kneaded.ai thesis.
3. **`/pilates.html`** — The Pilates Studio Custom Platform. The proof-of-concept case study.
4. **`/cyborg-workflow.html`** — The Cyborg Workflow. Two terminals, two Claudes.
5. **`/spec-is-the-hard-part.html`** — *new field note*, drawn from NVIDIA workshop posts. The "code isn't the hard part anymore — the spec is" + PM operating system thesis. This is Amir's strongest recent thinking and previously lived only on LinkedIn.

CCC banner placement: included on `/cyborg-workflow.html` and `/spec-is-the-hard-part.html` — both are tonally about parallel-Claude workflows where CCC is a natural fit. **Skipped on the small-business / pilates / guided-verification pages** because dropping a developer-tool ad on a Pilates-studio-owner-targeted page would feel forced.

### Salesy pages (`work-with-me.html`, `case-studies.html`, `about.html`, `packages.html`)
**Decision: replace contents with meta-refresh redirects to `/`.**

Reasoning: (a) CLAUDE.md says the style is being phased out; (b) the homepage already covers Advisory and Building; (c) outright `git rm` could break LinkedIn-bio links or other inbound URLs Amir has shared; (d) a redirect preserves SEO juice and link-equity while ending the visual mismatch. If Amir later wants typeset versions of any of these, the URLs are still available — they just bounce home for now.

The redirect pages keep a single `<noscript>` line so anyone with JS off (or a crawler) gets a clear "this page moved" message rather than a blank screen.

### Untouched
- `concept-*.html`, `compare-*.md`, `index-old-salesmachine.html` — sibling work or historical artifacts. Per the multi-agent git hygiene rule, I left them alone.
- `slides.html` — an older deck. Tone is off but it's only reachable if Amir links it. Out of scope.
- `main.js`, `styles.css` — kept on disk because the redirect pages don't load them, and other concept files might. Removing CSS is a bigger blast radius than the cleanup is worth in this session.

## What I did NOT do

- **Did not invent a Calendly link or pricing.** The CLAUDE.md briefing called this out as deliberately ambiguous. The Advisory CTA stays at `mailto:`.
- **Did not touch CCC repo content.** The `.ccc-card` references the existing GitHub repo and YouTube demo. No changes there.
- **Did not write new Pilates copy that wasn't already implied by the brief.** Pulled mostly from `CLAUDE.md` itself for the studio details.
- **Did not add a blog index page.** The homepage *is* the index — every Field Note links from there. Adding a separate `/writing` page would dilute the funnel.
- **Did not generate OG images.** Each new page has `og:title` / `og:description` set; image generation is a separate session.
- **Did not delete `concept-*.html` or other untracked files.** Sibling-session hygiene.

## Conversion path

Three doors visible from any new page:
1. **Star/install CCC** — `.ccc-card` on homepage + cyborg + spec pages; closing block on every field-note page.
2. **Read another Field Note** — homepage links + footer links between adjacent notes (where natural).
3. **Book advisory** — `mailto:amir@amirfish.com` from the homepage Advisory section + every page footer.

## Verification
- `curl -sI https://amirfish.ai/guided-verification | head -3` → expect 200
- Same for `/small-business-cofounder`, `/pilates`, `/cyborg-workflow`, `/spec-is-the-hard-part`
- `curl -sL https://amirfish.ai/work-with-me | grep -i 'amirfish.ai'` → should show meta-refresh
- `open https://amirfish.ai` and click each Field Note tile → should land on its page

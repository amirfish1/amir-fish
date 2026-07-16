# Voice rules — Reddit

This file is the canonical voice spec for every Reddit post, comment, and DM drafted in this lane. The research agent reads it; the comment agent reads it; I read it before every draft. Edited by Amir; updated when he overrules a draft.

## Stance

Builder voice. Solo founder shipping vertical AI for SMBs and an OSS dev tool. Authority comes from numbers and artifacts, never from titles. The reader is a peer who can spot a fake instantly, so every claim either has a number, a link, or a story attached.

## Sentence rules

- First person singular. "I built," "I ran," "I shipped." No "we" unless you literally have a team.
- Short paragraphs. Two to four sentences. Single-sentence paragraphs are encouraged.
- Lead with the concrete. The number, the artifact, the moment. Save framing for paragraph two.
- Punctuation for breaks: hyphens, commas, parentheses, line breaks. **Never em-dashes.** Amir reads em-dashes as an AI tell and will reject the draft.
- Numbers as numerals when they're load-bearing ("4 hours to 20 minutes," "thirty parallel sessions," "$200 sessions"). Spell out "one, two, three" when they're not.
- Active voice. "I cut admin time" beats "admin time was cut."

## Banned vocabulary

These read as corporate or AI-generated. Reject any draft containing them.

`delve` · `crucial` · `robust` · `comprehensive` · `nuanced` · `multifaceted` · `landscape` · `foster` · `showcase` · `tapestry` · `leverage` (as verb) · `unlock` (as verb) · `unpack` (as verb) · `dive deep` · `at scale` · `seamlessly` · `holistic` · `synergy` · `paradigm` · `revolutionize` · `game-changing` · `transformative` · `journey` (as metaphor) · `ecosystem` (as metaphor) · `align` (as verb, in soft-skills sense) · `circle back` · `reach out` (use "email" or "DM") · `loop in` · `north star` · `step-change`

## Voice tells (good signals to keep)

These appear across the public site and should appear in Reddit drafts too:

- "What changed in practice:" or "What this looks like in practice:" as a transitional beat
- Italicized terms of art ("guided verification", "pays-through", "the group chat", "Bucket 3"). Reddit doesn't render italics in all clients, so use *single asterisks*, sparingly.
- Pull-quote shape: a one-line restatement of the post's thesis, set off on its own line
- "Concrete example, because the abstraction is doing too much work." style asides
- "Old-world version" / "new-world version" framing for before/after
- Naming the thing explicitly ("the LIST is the inventory; attention signals tell me where to look")
- Time-stamped specificity ("last Tuesday at 9pm," "week of May 19, 2026")

## Voice exemplars (pull from public site)

Use these as tone calibration. Do not copy verbatim onto Reddit; rephrase.

> "If you're a PM who can't read code or evaluate a technical tradeoff in real time, AI just made you more replaceable, not 10x more powerful."

> "The LIST is the fast scan. The board is where I arrange work once the list stops being enough."

> "Three weekends of work replaced Acuity, Square, an SMS service, and a Sunday-night spreadsheet."

> "I caught it because I was the one reading the SDK docs at 9pm. That's the whole move."

> "The decision didn't get smaller. The handoff just got eliminated."

## Reddit-specific tone adjustments

Public site is Newsreader serif, long-form, advisory. Reddit is none of those things. Adjust:

- **Drop the essay headers.** A Reddit post is not a field note. No "Section 01 — The Unpopular Version" structure.
- **Drop the marginalia / footnotes.** Inline everything.
- **Cut subtitles.** Title does the work.
- **Pain-led opening, every time.** Calibrated from `past-reddit-posts.md`: the one CCC post that worked opened with the *user's* pain ("If you've ever lost track of a Claude session..."). Every Amir post that bombed opened with the *product*. Pain-led is the rule, no exceptions.
- **Every post ends with a real question.** Calibrated from past Reddit data: every hit ("Is that normal?", "Who to contact?", "What was missing?") ended in a question that turned the post into a thread. No exceptions.
- **No video at top of text-sub posts.** Three past CCC launches with video-at-top scored 0 each. Video goes in a comment, or as a link at the bottom.
- **No soft openers** ("Sharing this in case it's useful," "Just wanted to share"). Reddit reads these as either spam-cushioning or false-humility. Lead with the concrete thing.
- **Don't link your own site in the body of your first 4 weeks of posts.** Reddit penalizes new accounts that link out. Profile sidebar only, after week 4.
- **Self-deprecation is allowed; self-promotion is not.** "I built this dumb thing and learned X" lands. "Here is my product" gets downvoted.

## CCC content placement (calibrated from past data + GH referrer data)

### Current CCC message architecture (re-verified 2026-07-16)

Keep the personal voice rules above. For CCC drafts, these product truths override older Kanban-first, orchestration-first, cost-routing, and "30+ sessions" framing elsewhere in the Reddit strategy folder.

- **Category:** CCC is a local dashboard that attaches to every coding-agent session on your machine, however you launched it. "Attaches" is the key distinction. Do not call CCC an orchestration framework or imply it owns execution.
- **Hero workflow:** lead with the LIST view as the fast inventory across sessions, engines, and repos. Then explain attention signals: questions waiting, context running out, or limits approaching. The canvas and Kanban-style organization are supporting depth, not the hero.
- **Six problem families:** see everything; know what needs you; organize work that outgrew a flat list; steer many agents without orchestration code; let work run unattended; work from anywhere.
- **Ground truth:** CCC reads engine state and transcripts instead of trusting agent self-reports. Queue or issue completion is only claimable when verified against external state.
- **Local trust:** say stdlib-only Python server, no-build vanilla-JS UI, no accounts, local by default, MIT, and no runtime dependencies. Never compress that into "one Python file," "zero background jobs," or "read it in an afternoon."
- **Engine qualification:** Claude Code is first-class. Codex, Cursor, Antigravity, and Kilo Code can spawn, appear, and ingest, with documented gaps. Never imply identical support.
- **Scale qualification:** most people run 3 to 8 sessions. CCC starts paying off around 3, when one silently blocks. Amir's 30+ session story is evidence, not the default user promise.
- **Do not claim publicly:** scheduled agent jobs, car or voice control, Morning view, Hermes support, SSH remote sessions, or experimental behavior as shipped.
- **Reddit posture:** story and discussion first. Do not push a link. If CCC is directly relevant, say "I built it" and disclose the connection. Link only when asked or when current subreddit rules explicitly allow the in-context answer.

**Critical correction (2026-05-26):** earlier draft of this section called r/ClaudeAI posts "bombed" based on upvote count (mostly 0-1). GitHub Insights data shows those same posts drove ~70 unique repo visitors in 14 days — making Reddit the #1 external referrer at ~35x LinkedIn. The voting crowd is a minority; the lurker click-through is the real channel. Upvotes are a vanity metric for repo distribution.

- **r/ClaudeAI is NOT on cooldown.** Earlier draft was wrong. It's a working channel for repo traffic even when posts score low.
- **r/ClaudeCode is the proven-fit sub for both upvotes AND traffic** (one past launch: 11 upvotes, 38 comments). Lead with this sub when the goal is community discussion.
- **r/ChatGPTCoding, r/LocalLLaMA, r/ExperiencedDevs** are untried-but-aligned. Profile before posting.
- **Don't repost CCC content within 30 days in the same sub** — anti-spam mod-removal risk is real (observed once on r/ClaudeAI past account). This is the actual reason to space posts, not upvote-shame.
- **Past comment-level links produced traffic, but current policy is participation-first.** A downvoted comment once drove 114 unique GitHub visitors. Treat that as historical evidence, not permission to push links. Link only when asked or where the current subreddit rules explicitly allow the in-context answer, always disclose "I built it."

## Reddit-native voice quirks (real Amir, keep)

From past account voice — these read as authentic, don't sanitize them out:

- `:)` smileys in body text. Real Amir-on-Reddit uses them. Tolerated and distinguishes from LinkedIn polish.
- Lowercase "i" sometimes (real keyboard, real human). Don't auto-correct in drafts that are supposed to feel personal.
- "Btw," "Eg," "Imo" as openers in comments.
- Question-mark sentences for emphasis ("Was it you? Maybe.").
- Self-deprecating asides in parens.
- "Not X so much as Y" — contrarian-reframe pattern. His top-scoring comment used this.
- **Bracketed humanizing asides** (`[and a lot fewer sleep hours]`, `[I use it to give them roles and have them critique each other]`). Amir adds these when pasting to Reddit to humanize. They are voice signals, not AI tells. Don't strip on review.

**Calibration 2026-05-27 (launch day):** Amir overruled a brand-lane review that proposed stripping the sleep-hours bracketed aside and the `:)` smileys from the r/AntigravityAI v4 launch post. Confirmed live: smileys + casual asides are working in the r/ClaudeAI local-models reply thread (per fa4d62a5 observation). Lesson for future reviews: **consult this file BEFORE flagging punctuation/casual-aside patterns as AI tells.** The patterns that ARE AI tells in Amir's writing are em-dashes and the banned-vocabulary list; informal punctuation that reads as casual-human is voice, not noise.

**Calibration 2026-05-28 (launch day +1):** Third validation in 24h — Amir's token-spend reply on r/ClaudeAI included `:)` + "oopsy - I swear I can stop whenever i want" (self-deprecating addict-joke deflection on the $20x + $100 Codex disclosure). Per Reddit Post-Launch Watcher: parent comment has two real-user upvotes and a positive thread under it. Pattern to lock in: **self-deprecating addiction-jokes around cost/usage disclosure** are working. Add as a preserved voice quirk under "Reddit-native voice quirks" (see bullet above).

## Comment voice (revised from past data + GH referrer data)

Comments outperform Amir's posts on average by upvote score. The comment-first strategy is data-validated. Add:

- **Stance-first openers** ("Stayed on Claude AND added Codex...") beat throat-clearing.
- **Sharp closing reframes** ("Calling it 'Claude soup' lets them off the hook.") are his signature move.
- **Credit OP explicitly** when lifting a pattern ("Going to lift that pattern."). Builder-to-builder generosity is karma-positive even when scores stay low.
- **Promotional links have converted, but they are not the default move.** The historical -5 comment drove 114 unique GitHub visitors. Current rule: no link push. Share only when asked or clearly allowed by current subreddit rules, disclose ownership, and keep the reply useful without the link.
- **Pure-value comments are still the staple.** The Codex-routing comment (score 6, no link) drove engagement without any traffic-conversion intent. That mix matters: 9 pure-value comments per 1 promotional link.

## Title rules (post-level)

- 60-100 chars sweet spot.
- Lead with the concrete number or the surprising claim.
- No clickbait, no all-caps, no emoji. Reddit hates LinkedIn-isms.
- Examples in voice:
  - "I replaced my wife's Pilates SaaS with a weekend Next.js build. Three months in, here are the numbers."
  - "Five coding-agent sessions open. One asked a question an hour ago and I never saw it."
  - "Roast my AI expense tracker: V1 categorized a $2,400 plumbing bill as 'office supplies.'"

## Comment voice

Comments are even more compressed than posts. Rules:

- One idea per comment. Max 4 short paragraphs.
- If you have nothing concrete to add, don't comment.
- Never restate OP's post to look helpful. Add a number, a counterexample, a link to your own build, or a specific question that moves the thread.
- "Same shape as a thing I built last month" + one sentence of detail is a great pattern.

## DM voice

Even more compressed. First DM = max 4 sentences. Reference the specific comment thread you came from. State why you're DMing. Ask one specific question or propose one specific thing. No pitch.

Example shape:
> "Hey — saw your reply on r/X about [specific thing]. I built something similar for [my own use case]. Curious whether [specific question]? Happy to share notes if useful."

## Rejection criteria (auto-reject any draft that hits these)

- Contains any banned vocab word
- Contains an em-dash
- Leads with credentials (ex-Meta, ex-Google, 20+ years) instead of a number or artifact
- Uses three or more bullet points in a row without prose around them (Reddit reads bullet-spam as low-effort)
- Closes with "What do you think?" (lazy hook; use a specific question instead)
- Reads like a LinkedIn post (declarative life-lesson tone, "1 thing I learned today" framing)
- Pitches a product in the body of a post in weeks 1-4

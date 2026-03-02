# Amir Fish — Project Briefing & Handoff Document
**Last updated: February 28, 2026**

---

## Who Is Amir

Amir is an experienced product manager (20+ years) who previously served as Group PM at Meta and Group PM at Google, shipping AI products at scale. He left Meta ~6 months ago and is now building two interconnected businesses while developing a portfolio of AI-powered tools.

He lives in Sunnyvale, CA with his wife (who runs a Pilates studio) and children.

---

## The Two Businesses

### 1. AmirFish.com — AI Consulting
**Domain:** amirfish.com
**What it is:** Personal AI consulting brand offering "fractional CPO-level thinking" to Bay Area startups.
**Status:** Website is live but needs work. it's available on git. 
**Service tiers:**
- $200 strategy sessions
- fractional retainers

### 2. Kneaded.ai — AI-Powered Custom Software for Small Businesses
**Domain:** kneaded.ai (purchased for $159.99)
**What it is:** A platform/brand for delivering AI-powered custom software solutions to small businesses. The name "Kneaded" is a deliberate play — sounds like "needed," captures the hands-on craft of business building.
**Core thesis:** AI makes bespoke software economically viable for small businesses, ending the "one-size-fits-all" SaaS era. Every small business essentially gets a "technical co-founder" through AI-powered custom solutions.
**Status:** Brand established, domain purchased. Platform under development.

**Brand architecture:**
- AmirFish.com = personal consulting
- Kneaded.ai = small business platform & tools
- Personal finance apps = TBD placement (depends on whether they evolve toward personal or small business finance)

---

## The Proof-of-Concept: Inbar Fish Pilates (plts.xyz)

The foundational case study for the entire Kneaded.ai thesis. Amir built a complete custom business management platform for his wife's Pilates studio that replaced Acuity Scheduling entirely.

**Key results:**
- Reduced admin time from 4 hours/week to 20 minutes/week
- Eliminated payment processing fees via Venmo integration
- Built features no commercial platform would prioritize

**Features built:**
- Full scheduling & calendar system
- Venmo payment integration (zero processing fees vs Stripe/Square)
- "Pays-through" relationship — one client's Venmo pays for both a husband and wife, automatically reconciled
- Credit/package management
- SMS notifications & appointment reminders
- Client portal for rescheduling
- Public booking portal for new clients
- Receipt generation
- "Win-back" reminders for inactive clients
- WhatsApp booking integration

**Tech stack:** Next.js, deployed on Vercel. Built with Claude Code.
**GitHub repo:** inbar-fish-pilates (referenced in deploy logs)

---

## Other Apps Built

### Personal Finance App (sits in same domain as plts.xyz but needs to move somewhere)
- Expense tracking for rental properties and the Pilates business
- 1099 uploader with tax optimization (qualified vs non-qualified dividends)
- Brokerage portfolio review
- Bank connections (Plaid integration)
- Three-version evolution story: full automation → fully manual → "guided verification" (the winner)
- Deployed on Vercel as "my-finance-app"

### Marketing / Website Analysis Tools (will be in kneaded.ai)
- SEO analysis capabilities
- Dashboard and database cleanup tools
- Website analysis features for small businesses


---

## Key Intellectual Property / Thought Leadership

### The "Guided Verification" Framework
Amir's biggest UX insight, developed through building the expense tracker:
1. **V1 — Full automation:** AI categorizes everything. Looks great, silently wrong. A $2,400 plumbing repair miscategorized as "office supplies."
2. **V2 — Fully manual:** Accurate but soul-crushing. Nobody reviews 200 transactions monthly.
3. **V3 — Guided verification (winner):** System takes ownership of walking the user through decisions one at a time. Shows what it did, explains why, flags uncertainty, asks for confirmation. Result: 100% validated data in 10 minutes instead of 2 hours.

**His position:** This is THE UX challenge of the AI era. Most AI tools automate then dump results on users calling it "human in the loop" — that's just rubber-stamping, not real oversight.

### The AI Overpromise Monitoring Framework (from Mae)
At his previous company (Mae), Amir developed a 4-step framework that reduced AI overpromises from 15% to under 2% of conversations. He needs to be careful referencing this work since he's no longer with that company.

### The "Cyborg Workflow"
His development approach: Claude Code on one terminal writing Next.js logic + Claude browser extension on another terminal configuring third-party APIs (Stripe, Venmo webhooks, etc.) simultaneously. "Feels like having two senior engineers paired with me."

---

## Current Priorities & What Amir Needs

### organizing amirfish.com
- you can read it from git. 
- it's very "direct" right now, need to be much more subtle. Amir is an AI Expert and a veteran in Product management in strongest companies - shouldn't "sell" himself so hard. 

### Building in Public (LinkedIn)
- Actively posting "Personal Obsession" series on LinkedIn
- Targeting investors, VCs, and tech peers
- Topics covered: Pilates app story, guided verification insights, cyborg workflow
- Uses Claude with custom Style preset for drafting, then edits manually
- Prefers authentic/conversational tone, avoids polished "AI voice"

### Platform Development (Kneaded.ai)
- Needs to evolve from individual bespoke builds to a scalable platform
- The Pilates studio is the anchor case study
- Exploring how to productize the "AI-powered custom software" offering

### Networking & Startup Ecosystem
- Participated in Dreamer Virtual Hackathon (demo'd Pilates management system)
- Attending Bay Area networking events to find potential customers, partners, and referral sources
- Has early access to Dreamer AI (Hugo Barra & David Singleton's no-code agent platform)

---

## Development Environment & Tools

- **Primary dev tool:** Claude Code (CLI)
- **Browser automation:** Claude browser extension
- **Hosting:** Vercel
- **Code:** Next.js / React
- **Payments:** Stripe (consulting site), Venmo (Pilates app)
- **Domain management:** GoDaddy, ImprovMX (email forwarding for amirfish.com)
- **Version control:** GitHub
- **Prototyping:** Dreamer AI (early access)

---

## Communication Style Notes

- Conversational, not corporate
- Prefers prescriptive recommendations over open-ended options
- Appreciates when tools/AI are direct about what's best
- Iterates fast — "deploy by lunch" mentality
- Values authenticity; allergic to polished AI-sounding content
- Runs a "Personal Obsession" LinkedIn series with numbered entries
- Uses bold unicode text formatting in LinkedIn posts for emphasis

---

## Key Contacts Referenced

- **Todd Markez** — Former Google colleague, potential co-founder/collaborator
- **Amir Shevat** — Co-Founder/CTO at Dark Mode VC, had a meeting scheduled
- **Amit Attias** — Co-Founder/CTO at Bigabid, tried reaching Amir on LinkedIn
- **Tong Liu** — Google Cloud GenAI Engineering, networking contact
- **Dean Mordechai** — Colleague from Mae, handles bug tickets on Monday.com

---

## Open Questions / Decisions Pending

1. **Where does the personal finance app live?** Under Kneaded.ai or separate? Depends on whether it evolves toward small business finance tools.
2. **How to scale from bespoke builds to a platform?** The Pilates app proves the thesis, but Kneaded.ai needs a repeatable delivery model.
3. **Todd Markez collaboration scope** — What role could Todd play? Co-founder? Advisor? Customer intro network?
4. **Monetization path for Kneaded.ai** — Per-project builds? Monthly retainer? Platform subscription?
5. **Mae IP boundaries** — How much of the AI monitoring framework can Amir reference publicly without crossing lines with his former employer?

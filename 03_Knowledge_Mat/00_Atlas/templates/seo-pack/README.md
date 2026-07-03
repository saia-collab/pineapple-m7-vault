# SEO Content Pipeline Pack — AIPB Edition

This pack contains everything you need to run the same 5-site SEO content pipeline used inside the AI Profit Boardroom community.

## 📂 What's inside

- **`blog-post.md`** — the Claude skill that writes your 5 posts. Customise the brand voice section and video library, then drop it into your main site's `.claude/skills/` folder.
- **`seoPipeline.ts.template`** — config snippet Agentic OS reads to find your 5 sites. Replace the placeholders with your real domain names and folder paths, then paste it into `src/lib/seoPipeline.ts` in your Agentic OS repo.
- **`example-transcript.txt`** — a sample transcript so you can see the format Claude expects.
- **`README.md`** — this file.

## 🚀 Quick start

1. Follow the full guide at **Agentic OS → SEO Setup Guide** (or in `SEO-SETUP.md`).
2. Customise `blog-post.md` with your brand voice + video library.
3. Drop `blog-post.md` into `~/your-main-site/.claude/skills/`.
4. Replace the 5 site entries in `seoPipeline.ts.template` with your domains.
5. Paste the updated config into `src/lib/seoPipeline.ts` inside your Agentic OS repo.
6. Restart Agentic OS (`npm run dev`).
7. Open the SEO tab — your sites should appear.
8. Drop a transcript into your main site's `.claude/transcripts/` folder.
9. In the SEO tab, click **Generate**, pick the transcript, click **Generate Posts**.
10. When it's done, click **Deploy All**.

## 🛟 Need help?

- Full step-by-step guide: open Agentic OS → SEO tab → **Setup Guide** button
- Community: [skool.com/ai-profit-lab-7462/about](https://www.skool.com/ai-profit-lab-7462/about)

## 📜 Licence

Complimentary to use for AIPB members and the wider community. Adapt to your own brand. Don't republish the pack itself — just point people to AIPB.

— Julian Goldie

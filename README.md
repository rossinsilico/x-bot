# Daily Dispatch Bot 🧠📬

A local-first AI agent that generates daily tweet drafts in your voice and delivers them via email or an optional Electron UI. Built for privacy, reliability, and dev joy.

## ✨ Features

- ✅ Runs daily via cron at 8AM with fallback retries
- ✅ Fetches your tweets and learns your style
- ✅ Generates tweet drafts using local LLMs (via Ollama) or OpenAI
- ✅ Delivers suggestions via email each morning
- ✅ Optional Electron UI for local review, editing, and approvals
- ✅ Fully offline-capable and idempotent (won’t run twice per day)

## 📁 Project Structure

```bash
ross-daily-dispatch/
├── main.py                # Orchestration script (runs daily)
├── fetcher.py             # Grabs recent tweets
├── analysis.py            # Style profiling + sentiment/topic modeling
├── generator.py           # LLM prompt building + tweet generation
├── reviewer.py            # Optional local Electron/CLI review
├── poster.py              # (Optional) posting module
├── utils/
│   └── emailer.py         # Email sender
├── data/
│   ├── tweets.json
│   ├── style_profile.json
│   ├── last_sent.json
│   └── drafts_YYYY-MM-DD.txt
├── config.yaml            # Runtime settings (model, cron prefs)
├── .env                   # API keys (OpenAI, Twitter)
└── README.md

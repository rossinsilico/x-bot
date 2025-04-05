# X-Bot: Daily Dispatch Automation

This project automates the process of fetching, analyzing, generating, and posting tweets. It also includes optional features like email digests and a review interface.

## Features
- Fetch Twitter content.
- Analyze style, tone, sentiment, and topics.
- Generate tweets using LLMs.
- Optional review and posting interfaces.
- Daily digest email support.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure `.env` and `config.yaml`.

3. Schedule the script using cron (see `config/cron_setup.md`).

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

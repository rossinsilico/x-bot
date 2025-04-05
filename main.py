# main.py
# x-bot: Daily Dispatch Script
# This script generates tweets using OpenAI or Ollama, saves them to a file, and optionally sends them via email.
# It also checks if the script has already been run today to avoid duplicate processing.
import os
from datetime import datetime
from utils.time_check import already_sent_today, mark_sent
from generator import generate_tweets
from utils.emailer import send_daily_email
import yaml

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

def run():
    print("🤖 Starting x-bot daily dispatch...")

    if already_sent_today():
        print("✅ Already processed today. Skipping.")
        return

    # Generate tweets (OpenAI or Ollama)
    drafts = generate_tweets(config)

    # Save drafts
    date_str = datetime.now().strftime("%Y-%m-%d")
    os.makedirs("data", exist_ok=True)
    file_path = f"data/drafts_{date_str}.txt"
    with open(file_path, "w") as f:
        f.write("\n\n".join(drafts))

    print(f"📝 Saved {len(drafts)} drafts to {file_path}")

    if config.get("use_email", True):
        send_daily_email(drafts)

    mark_sent()
    print("🚀 Dispatch complete.")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"❌ Error: {e}")
        with open("data/error.log", "a") as log:
            log.write(f"[{datetime.now()}] {str(e)}\n")
# x-bot: Daily Dispatch Script
# This script generates tweets using OpenAI or Ollama, saves them to a file, and optionally sends them via email.
# It also checks if the script has already been run today to avoid duplicate processing.
import os
from datetime import datetime
from utils.time_check import already_sent_today, mark_sent
from generator import generate_tweets
from utils.emailer import send_daily_email
from dotenv import load_dotenv
load_dotenv()
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--force", action="store_true")
args = parser.parse_args()

def run():
    print("🤖 Starting x-bot daily dispatch...")

    if not args.force and already_sent_today():
        print("✅ Already processed today. Skipping.")
        return
    # Generate tweets (OpenAI or Ollama)
    drafts = generate_tweets()

    # Save drafts
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = f"data/drafts_{date_str}.txt"
    os.makedirs("data", exist_ok=True)
    with open(file_path, "w") as f:
        f.write("\n\n".join(drafts))

    print(f"📝 Saved {len(drafts)} drafts to {file_path}")

    # Optional: Email dispatch (currently always on)
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

# This script generates tweets using OpenAI or Ollama, saves them to a file, and optionally sends them via email.
# It also checks if the script has already been run today to avoid duplicate processing.
# The script uses environment variables for SMTP configuration and loads them using dotenv.
# It generates tweets based on a configuration file and saves them in a specific format.
# The script also handles errors and logs them to a file.
# The script is designed to be run as a standalone program and will execute the main function when run directly.
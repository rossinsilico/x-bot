# utils/emailer.py
# x-bot: Daily Dispatch Script
# This script generates tweets using OpenAI or Ollama, saves them to a file, and optionally sends them via email.
# It also checks if the script has already been run today to avoid duplicate processing.

import os
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv

load_dotenv()

def send_daily_email(drafts):
    sender = os.getenv("SMTP_USER")
    recipient = os.getenv("SMTP_USER")  # sending to yourself

    body = "\n\n".join(drafts)
    subject = "Ross’s Daily Dispatch – Drafts Ready"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))) as server:
            server.login(sender, os.getenv("SMTP_PASS"))
            server.send_message(msg)
        print("📬 Email sent successfully.")
    except Exception as e:
        print(f"❌ Email failed: {e}")
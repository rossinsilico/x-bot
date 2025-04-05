import os
import json
from datetime import datetime

STATUS_FILE = "data/last_sent.json"

def already_sent_today():
    if not os.path.exists(STATUS_FILE):
        return False
    try:
        with open(STATUS_FILE, "r") as f:
            data = json.load(f)
        return data.get("date") == datetime.now().strftime("%Y-%m-%d")
    except Exception:
        return False

def mark_sent():
    os.makedirs("data", exist_ok=True)
    with open(STATUS_FILE, "w") as f:
        json.dump({"date": datetime.now().strftime("%Y-%m-%d")}, f)

#!/usr/bin/env bash

# ↪️ go to your project dir
cd /Users/rosspingatore/Dev/x-bot

LOG_FILE="data/cron.log"

# ↪️ log start
echo "[$(date)] Starting x-bot from cron..." >> "$LOG_FILE"

# ↪️ activate Conda env
source ~/miniconda3/etc/profile.d/conda.sh
conda activate x-bot

# ↪️ fetch latest tweets/archive
python fetcher.py >> "$LOG_FILE" 2>&1

# ↪️ run the main dispatch (passes --force if you invoked it)
python main.py "$@" >> "$LOG_FILE" 2>&1

# ↪️ log end
echo "[$(date)] x-bot finished run" >> "$LOG_FILE"
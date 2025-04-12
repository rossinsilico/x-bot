#!/bin/bash

echo "[$(date)] Starting x-bot from cron..." >> /Users/rosspingatore/Dev/x-bot/data/cron.log

source ~/miniconda3/etc/profile.d/conda.sh
conda activate x-bot

python /Users/rosspingatore/Dev/x-bot/main.py "$@" >> /Users/rosspingatore/Dev/x-bot/data/cron.log 2>&1

echo "[$(date)] x-bot finished run" >> /Users/rosspingatore/Dev/x-bot/data/cron.log

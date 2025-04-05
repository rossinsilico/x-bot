# Instructions for setting up cron jobs to run the application.

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following line to schedule the script:
   ```bash
   0 9 * * * python3 /path/to/main.py
   ```

3. Save and exit.

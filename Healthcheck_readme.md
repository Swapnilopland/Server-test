# Website Health Monitor

## Description
This script continuously checks website availability and sends email alerts when downtime is detected.

## Setup
1. Install dependencies:
   ```bash
   pip install requests
2. Configure:

Update WEBSITE_URL with your target URL

Set up SMTP credentials in SMTP CONFIG

Add recipient emails in ALERT_EMAILS


USAGE
python healthcheck.py

Run as a background service:
nohup python healthcheck.py > healthcheck.log 2>&1 &

Schedule checks (linux)
*/5 * * * * /usr/bin/python3 /path/to/healthcheck.py >> /path/to/healthcheck.log 2>&1

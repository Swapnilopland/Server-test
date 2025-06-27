What to Monitor**:
- **Failure Rate** > 1% → Application bugs
- **Response Time** > 5s → Database/CPU bottleneck
- **Error Types**:
  - `HTTP 500` → Code exceptions
  - `HTTP 502/503` → Azure infrastructure issues

# Load Testing with Locust

## Description
Simulates user traffic to identify performance bottlenecks.

## Setup
1. Install Locust:
   ```bash
   pip install locust

   2. Configure:

Update WebsiteUser tasks to match your endpoints

Modify login credentials if needed

USAGE 
Quick Test(terminal)
locust -f loadtest.py --headless -u 100 -r 10 --host http://demo.otplx.com

Interactive Dashboard
locust -f loadtest.py --host http://demo.otplx.com

Access: http://localhost:8089

Reports

CSV reports are generated automatically:

loadtest stats.csv

loadtest failures.csv

---

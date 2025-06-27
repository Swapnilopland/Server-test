from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Random wait between requests

    @task(3)  # Weighted priority
    def view_timesheet(self):
        self.client.get("/timesheet", name="Timesheet Page")

    @task(2)
    def submit_form(self):
        payload = {
            "date": "2023-10-05",
            "hours": random.randint(1, 24),
            "project_id": random.randint(1, 100)
        }
        self.client.post("/timesheet", json=payload, name="Submit Timesheet")

    @task(1)
    def generate_report(self):
        self.client.get("/report?type=pdf", name="PDF Report")

    def on_start(self):
        # Login once per user
        self.client.post("/login", data={
            "email": "cm@oplandtech.com",
            "password": "Abcd1234*"
        })

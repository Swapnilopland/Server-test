import requests
import time
from datetime import datetime
import smtplib  # For email alerts

# Configuration
WEBSITE_URL = "http://demo.otplx.com"
CHECK_INTERVAL = 60  # Seconds
DEPENDENCIES = {
    "Database": "your-database.database.windows.net",
    "Storage": "yourstorage.blob.core.windows.net"
}

def check_endpoint(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Error checking {url}: {str(e)}")
        return False

def send_alert(message):
    # Configure your SMTP (e.g., SendGrid, Office 365)
    with smtplib.SMTP("smtp.yourprovider.com", 587) as server:
        server.login("alerts@yourdomain.com", "yourpassword")
        server.sendmail(
            "alerts@yourdomain.com",
            "admin@yourdomain.com",
            f"Subject: Website Alert\n\n{message}"
        )

def main():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Check website
        if not check_endpoint(WEBSITE_URL):
            error_msg = f"[{timestamp}] Website DOWN: {WEBSITE_URL}"
            print(error_msg)
            send_alert(error_msg)
        
        # Check dependencies
        for name, endpoint in DEPENDENCIES.items():
            if not check_endpoint(f"https://{endpoint}/health"):
                error_msg = f"[{timestamp}] Dependency FAILED: {name} ({endpoint})"
                print(error_msg)
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

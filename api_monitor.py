import requests
import os
import time


API_URL = os.getenv("API_URL") 
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") 
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def check_api():
    try:
        response = requests.get(API_URL, timeout=60)
        if response.status_code != 200:
            send_alert(f"🔴 API DOWN: Status Code {response.status_code}")
        else:
            print(f"✅ API OK: {response.status_code}")
    except requests.exceptions.RequestException as e:
        send_alert(f"🔴 API ERROR: {str(e)}")

def send_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, json=payload)
        print(f"Alert sent: {message}")
    except Exception as e:
        print(f"Failed to send Telegram alert: {e}")

if __name__ == "__main__":
    check_api()
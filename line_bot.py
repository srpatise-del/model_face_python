import os
import requests
from dotenv import load_dotenv

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
LINE_URL = "https://api.line.me/v2/bot/message/push"

headers = {
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

USER_FILE = "users.txt"

def send_text(message):

    if not os.path.exists(USER_FILE):
        print("users.txt not found")
        return

    with open(USER_FILE, "r", encoding="utf-8") as f:
        users = [u.strip() for u in f.readlines() if u.strip()]

    for user_id in users:

        body = {
            "to": user_id,
            "messages": [
                {
                    "type": "text",
                    "text": message
                }
            ]
        }

        r = requests.post(
            LINE_URL,
            headers=headers,
            json=body
        )

        print(user_id, r.status_code)
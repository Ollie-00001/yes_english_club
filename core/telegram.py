import os
import requests
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = getattr(settings, 'TELEGRAM_BOT_TOKEN', os.getenv('TELEGRAM_BOT_TOKEN'))
TELEGRAM_CHAT_ID = getattr(settings, 'TELEGRAM_CHAT_ID', os.getenv('TELEGRAM_CHAT_ID'))

def send_telegram_message(text: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials not set")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        print("Sending Telegram message:\n", text)
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        print("Message sent successfully")
    except Exception as e:
        print("Error sending Telegram message:", e)
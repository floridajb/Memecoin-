import requests
import time
from datetime import datetime

# ================== FILL THESE IN ==================
TELEGRAM_TOKEN = 8605435024
CHAT_ID = 8239472481
# ===================================================

# Settings you can change
MAX_MARKET_CAP = 15000
MIN_LIQUIDITY = 2000
SCAN_INTERVAL = 60          # seconds between scans
MAX_TOKENS_PER_SCAN = 20

DEX_BASE = "https://api.dexscreener.com"
RUGCHECK_BASE = "https://api.rugcheck.xyz/v1"

def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Telegram error: {e}")

def get_latest_profiles():
    try:
        r = requests.get(f"{DEX_BASE}/token-

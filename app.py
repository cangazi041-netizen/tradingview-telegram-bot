from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)

        text = f"""
{data['side']} SIGNAL

Symbol: {data['symbol']}
TF: {data['tf']}
Entry: {data['entry']}
SL: {data['sl']}
TP1: {data['tp1']}
TP2: {data['tp2']}
"""

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": text
        }

        requests.post(url, json=payload)

        return {"status": "ok"}, 200

    except Exception as e:
        print("Error:", e)
        return {"status": "error"}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

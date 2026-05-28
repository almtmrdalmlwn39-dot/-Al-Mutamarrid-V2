from pyrogram import Client
from flask import Flask
from threading import Thread

# 1. تعريف البوت
app = Client(
    "almtmrd_bot",
    api_id=22610186,
    api_hash="184e7fd176413cd0d2425494f1796229",
    bot_token="8762367853:AAFoyDjc55d0fPTvRThmDFh8_wsQY39Br9g",
    plugins=dict(root="plugins")
)

# 2. تعريف السيرفر (بسيط جداً)
server = Flask(__name__)
@server.route("/")
def home():
    return "البوت يعمل!"

# 3. تشغيل السيرفر في خلفية منفصلة
def run_server():
    server.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    Thread(target=run_server).start()
    app.run()

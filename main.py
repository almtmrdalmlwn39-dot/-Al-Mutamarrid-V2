import os
from flask import Flask
from pyrogram import Client
from threading import Thread

# 1. إعداد السيرفر
app_flask = Flask('')
@app_flask.route('/')
def home():
    return "البوت يعمل الآن!"

def run_server():
    app_flask.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# 2. تشغيل السيرفر في Thread منفصل
Thread(target=run_server).start()

# 3. إعداد البوت
app = Client(
    "almtmrd_bot",
    api_id=22610186,
    api_hash="184e7fd176413cd0d2425494f1796229",
    bot_token="8762367853:AAFoyDjc55d0fPTvRThmDFh8_wsQY39Br9g",
    plugins=dict(root="plugins")
)

# 4. تشغيل البوت الأساسي
app.run()

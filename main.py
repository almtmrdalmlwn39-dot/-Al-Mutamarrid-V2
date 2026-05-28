import os
from flask import Flask
from pyrogram import Client
from threading import Thread

# 1. إعداد السيرفر
app_flask = Flask('')
@app_flask.route('/')
def home(): return "البوت يعمل الآن!"
def run(): app_flask.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# 2. تشغيل السيرفر في الخلفية
Thread(target=run).start()

# 3. بيانات البوت الموحدة
API_ID = 22610186
API_HASH = "184e7fd176413cd0d2425494f1796229"
BOT_TOKEN = "8762367853:AAFoyDjc55d0fPTvRThmDFh8_wsQY39Br9g"

# 4. تشغيل البوت (بشكل مباشر)
app = Client(
    "almtmrd_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

app.run()

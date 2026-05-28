import os
from threading import Thread
from flask import Flask
from pyrogram import Client

# 1. إعدادات سيرفر الحماية (Render)
flask_app = Flask('')
@flask_app.route('/')
def home(): return "البوت يعمل الآن!"
def run(): flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# 2. تعريف البوت (خارج الـ if لضمان تحميل الـ plugins)
app = Client(
    "almtmrd_bot",
    api_id=22610186,
    api_hash="184e7fd176413cd0d2425494f1796229",
    bot_token="8762367853:AAFoyDjc55d0fPTvRThmDFh8_wsQY39Br9g", # تأكد أن هذا هو التوكن الصحيح
    plugins=dict(root="plugins")
)

# 3. التشغيل النهائي
if __name__ == "__main__":
    keep_alive()
    app.run()

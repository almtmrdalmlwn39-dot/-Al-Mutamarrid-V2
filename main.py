import os
from threading import Thread
from flask import Flask
from pyrogram import Client

# سيرفر الحماية لـ Render
flask_app = Flask('')
@flask_app.route('/')
def home(): return "البوت يعمل الآن!"
def run(): flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# تشغيل البوت بالبيانات المحدثة
if __name__ == "__main__":
    keep_alive()
    app = Client(
        "almtmrd_bot",
        api_id=22610186,
        api_hash="184e7fd176413cd0d2425494f1796229",
        bot_token="7295980036:AAGR8wQYmX_uS_4-YF2D6tQpB2V_m_e-S_A",
        plugins=dict(root="plugins")
    )
    app.run()

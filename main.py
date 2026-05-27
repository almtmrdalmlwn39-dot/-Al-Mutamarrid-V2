import os
from threading import Thread
from flask import Flask
from pyrogram import Client

# سيرفر الحماية
flask_app = Flask('')
@flask_app.route('/')
def home(): return "البوت يعمل!"
def run(): flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# تشغيل البوت مع ربط مجلد الـ plugins
app = Client(
    "almtmrd_bot",
    api_id=26588241,
    api_hash="b90956461a510523097f48030999554b",
    bot_token="7295980036:AAGR8wQYmX_uS_4-YF2D6tQpB2V_m_e-S_A",
    plugins=dict(root="plugins") # هذا السطر هو جوهر الربط
)

if __name__ == "__main__":
    keep_alive()
    app.run()

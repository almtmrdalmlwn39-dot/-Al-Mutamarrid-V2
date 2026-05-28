import os
import asyncio
from flask import Flask
from pyrogram import Client
from threading import Thread

# 1. إعداد السيرفر ليعمل في خيط منفصل (Thread)
app_flask = Flask('')
@app_flask.route('/')
def home(): return "البوت يعمل!"

def run_server():
    app_flask.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

Thread(target=run_server).start()

# 2. إعداد البوت
app = Client(
    "almtmrd_bot",
    api_id=22610186,
    api_hash="184e7fd176413cd0d2425494f1796229",
    bot_token="8762367853:AAFoyDjc55d0fPTvRThmDFh8_wsQY39Br9g",
    plugins=dict(root="plugins")
)

# 3. تشغيل البوت بطريقة متوافقة مع الـ Event Loop
async def main():
    await app.start()
    print("البوت بدأ العمل!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

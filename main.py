import os
from pyrogram import Client, filters
from aiohttp import web

# إعداد المنفذ
PORT = int(os.environ.get("PORT", 8080))

# إعداد البوت
app = Client(
    "my_bot", 
    api_id=22610186, 
    api_hash="184e7fd176413cd0d2425494f1796229", 
    bot_token="8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I"
)

# أمر تجريبي بسيط
@app.on_message(filters.command("اختبار"))
async def test(client, message):
    await message.reply_text("البوت يعمل! ✅")

# تشغيل البوت مع الويب
async def start_bot():
    app_web = web.Application()
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    await app.start()
    print("البوت جاهز للعمل!")
    await app.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_bot())

import os
from pyrogram import Client
from aiohttp import web

# إعداد المنفذ الذي يطلبه Render
PORT = int(os.environ.get("PORT", 8080))

async def handle(request):
    return web.Response(text="Bot is running")

app = Client(
    "my_bot", 
    api_id=22610186, 
    api_hash="184e7fd176413cd0d2425494f1796229", 
    bot_token="8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I",
    plugins=dict(root="plugins") 
)

async def start_bot():
    # تشغيل خادم الويب لاسترضاء Render
    runner = web.AppRunner(web.Application())
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    
    # تشغيل البوت
    await app.start()
    print("البوت يعمل الآن!")
    await app.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_bot())

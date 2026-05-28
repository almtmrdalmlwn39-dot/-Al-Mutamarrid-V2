from pyrogram import Client
from aiohttp import web
import asyncio
import logging
import traceback

logging.basicConfig(level=logging.INFO)

app = Client(
    "almtmrd_bot",
    api_id=22610186,
    api_hash="184e7fd176413cd0d2425494f1796229",
    bot_token="8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I",
    plugins=dict(root="plugins")
)

async def handle(request):
    return web.Response(text="Bot is running")

async def run_bot():
    # تشغيل سيرفر الويب الوهمي لإرضاء Render
    app_web = web.Application()
    app_web.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    
    # تشغيل البوت
    await app.start()
    print("البوت بدأ العمل الآن بنجاح!")
    await asyncio.gather(app.idle())

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except Exception:
        traceback.print_exc()

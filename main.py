from pyrogram import Client
from aiohttp import web
import asyncio

# التوكن الخاص بك
TOKEN = "8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I"

app = Client(
    "my_bot", 
    api_id=22610186, 
    api_hash="184e7fd176413cd0d2425494f1796229", 
    bot_token=TOKEN,
    plugins=dict(root="plugins") 
)

# هذا الجزء يخدع Render ويخبره أن البوت يعمل ويفتح منفذ 8080
async def handle(request):
    return web.Response(text="Bot is running")

async def run_bot():
    app_web = web.Application()
    app_web.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    
    await app.start()
    print("البوت يعمل الآن بنجاح!")
    await app.idle()

if __name__ == "__main__":
    asyncio.run(run_bot())

from pyrogram import Client, filters

# التوكن الخاص بك
TOKEN = "8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I"

app = Client("my_bot", api_id=22610186, api_hash="184e7fd176413cd0d2425494f1796229", bot_token=TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("البوت يعمل بنجاح!")

app.run()

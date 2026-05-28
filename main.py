from pyrogram import Client

# التوكن الخاص بك
TOKEN = "8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I"

# ربط البوت بمجلد الـ plugins
app = Client(
    "my_bot", 
    api_id=22610186, 
    api_hash="184e7fd176413cd0d2425494f1796229", 
    bot_token=TOKEN,
    plugins=dict(root="plugins") # هذا السطر هو السر!
)

app.run()

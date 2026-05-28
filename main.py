import os
from pyrogram import Client

# قراءة البيانات من المتغيرات في Render أو القيم الافتراضية
app = Client(
    "my_bot",
    api_id=int(os.environ.get("API_ID", 22610186)),
    api_hash=os.environ.get("API_HASH", "184e7fd176413cd0d2425494f1796229"),
    bot_token=os.environ.get("BOT_TOKEN", "8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I"),
    plugins=dict(root="plugins")
)

app.run()

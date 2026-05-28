from pyrogram import Client

# إعداد البوت
api_id = 22610186
api_hash = "184e7fd176413cd0d2425494f1796229"
bot_token = "8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I"

# ربط المجلد باسمه الصحيح (تأكد أن المجلد اسمه plugins بحروف صغيرة)
app = Client(
    "my_bot", 
    api_id=api_id, 
    api_hash=api_hash, 
    bot_token=bot_token,
    plugins=dict(root="plugins")
)

print("البوت يعمل الآن بنظام الـ Plugins...")
app.run()

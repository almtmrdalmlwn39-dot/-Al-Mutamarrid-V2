from pyrogram import Client
import logging
import traceback # أضفنا هذه المكتبة

logging.basicConfig(level=logging.INFO)

app = Client(
    "almtmrd_bot",
    api_id=22610186,
    api_hash="184e7fd176413cd0d2425494f1796229",
    bot_token="8762367853:AAH5769kMPrIrvTGr1aOTYnUwF2nfvzcp4I",
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    try:
        print("البوت بدأ العمل الآن...")
        app.run()
    except Exception as e:
        print("--- حدث خطأ قاتل ---")
        traceback.print_exc() # هذا السطر سيجبر البوت على كتابة نوع الخطأ ومكانه بالتفصيل

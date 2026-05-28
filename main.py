from pyrogram import Client
import logging

# إعداد السجلات لمراقبة الأخطاء
logging.basicConfig(level=logging.INFO)

# إعداد البوت
app = Client(
    "almtmrd_bot",
    api_id=22610186,
    api_hash="184e7fd176413cd0d2425494f1796229",
    bot_token="8762367853:AAFoyDjc55d0fPTvRThmDFh8_wsQY39Br9g",
    plugins=dict(root="plugins")
)

# تشغيل البوت مباشرة
if __name__ == "__main__":
    print("البوت بدأ العمل الآن...")
    app.run()

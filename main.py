import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# --- سيرفر وهمي لمنع توقف ريندر ---
flask_app = Flask('')
@flask_app.route('/')
def home(): return "البوت يعمل!"

def run(): flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# --- بيانات البوت ---
API_ID = 22610186
API_HASH = "184e7fd176413cd0d2425494f1796229"
BOT_TOKEN = "8762367853:AAFoyDjc55d0fPTvRThmDFh8_wsQY39Br9g"

app = Client("almtmrd_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

MENU_TEXT = """
**- أهلاً بك عزيزي في قائمة الاوامر :**
━━━━━━━━━━━━
◂ م1 : اوامر الادمنيه
◂ م2 : اوامر الاعدادات
◂ م3 : اوامر القفل - الفتح
◂ م4 : اوامر التسليه
◂ م5 : اوامر Dev
◂ م6 : الاوامر الخدميه 
━━━━━━━━━━━━
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("م1", callback_data="m1"), InlineKeyboardButton("م2", callback_data="m2"), InlineKeyboardButton("م3", callback_data="m3")],
        [InlineKeyboardButton("م4", callback_data="m4"), InlineKeyboardButton("م5", callback_data="m5"), InlineKeyboardButton("م6", callback_data="m6")],
        [InlineKeyboardButton("• قـناة الـسورس •", url="https://t.me/A0_07")]
    ]
)

@app.on_message(filters.command(["start", "الاوامر"]))
async def start(client, message):
    await message.reply_text(MENU_TEXT, reply_markup=START_BUTTONS)

@app.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    if query.data == "m1":
        await query.message.edit_text("**قائمة الإدمنية شغالة يا بطل!**", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    elif query.data == "main":
        await query.message.edit_text(MENU_TEXT, reply_markup=START_BUTTONS)

if __name__ == "__main__":
    keep_alive() # تشغيل السيرفر المساعد
    app.run()

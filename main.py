from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# بيانات البوت (جاهزة)
API_ID = 22610186
API_HASH = "184e7fd176413cd0d2425494f1796229"
BOT_TOKEN = "8794844755:AAHA6yvFrM2rEm6A2II1LlenrFOl8ZjfGVE"

app = Client("almtmrd_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# نص القائمة
START_TEXT = """
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

# الأزرار الشفافة
START_BUTTONS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("1", callback_data="m1"), InlineKeyboardButton("2", callback_data="m2"), InlineKeyboardButton("3", callback_data="m3")],
        [InlineKeyboardButton("4", callback_data="m4"), InlineKeyboardButton("5", callback_data="m5"), InlineKeyboardButton("6", callback_data="m6")],
        [InlineKeyboardButton("• قـناة الـسورس •", url="t.me/A0_07")]
    ]
)

@app.on_message(filters.command("start") | filters.command("الاوامر"))
async def start(client, message):
    await message.reply_text(START_TEXT, reply_markup=START_BUTTONS)

@app.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    if query.data == "m1":
        await query.answer("قائمة الادمنيه قادمة..", show_alert=True)
    # يمكنك إضافة الباقي هنا

# أهم سطر للتشغيل (هذا الذي كان ينقصك)
app.run()

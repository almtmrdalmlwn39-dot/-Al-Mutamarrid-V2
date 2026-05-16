from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# بيانات البوت الخاصة بك من الصور
API_ID = 22610186
API_HASH = "184e7fd176413cd0d2425494f1796229"
BOT_TOKEN = "8794844755:AAHA6yvFrM2rEm6A2II1LlenrFOl8ZjfGVE"

app = Client("almtmrd_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# النص الرئيسي للقائمة
START_TEXT = """
**- ‌‌‏أهلاً بك عزيزي في قائمة الاوامر :**
━━━━━━━━━━━━
◂ م1 : اوامر الادمنيه
◂ م2 : اوامر الاعدادات
◂ م3 : اوامر القفل - الفتح
◂ م4 : اوامر التسليه
◂ م5 : اوامر Dev
◂ م6 : الاوامر الخدميه 
━━━━━━━━━━━━
"""

# تصميم الأزرار (تعديل رقم 8 إلى 6 وتنسيق احترافي)
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("1", callback_data="m1"),
            InlineKeyboardButton("2", callback_data="m2"),
            InlineKeyboardButton("3", callback_data="m3")
        ],
        [
            InlineKeyboardButton("4", callback_data="m4"),
            InlineKeyboardButton("5", callback_data="m5"),
            InlineKeyboardButton("6", callback_data="m6")
        ],
        [
            InlineKeyboardButton("• الـمـطـور •", url="t.me/A0_07"),
            InlineKeyboardButton("• تـحديثات الـمتمرد •", url="t.me/A0_07")
        ]
    ]
)

@app.on_message(filters.command("الاوامر"))
async def start(client, message):
    await message.reply_text(START_TEXT, reply_markup=START_BUTTONS)

@app.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    if query.data == "main":
        await query.message.edit_text(START_TEXT, reply_markup=START_BUTTONS)
    
    elif query.data == "m1":
        await query.message.edit_text("**قائمة اوامر الادمنيه**\n━━━━━━━━━━━━\n• رفع - تنزيل (مالك، مدير، ادمن..)\n• مسح (المحظورين، الردود، الرسائل)\n• طرد، حظر، كتم، تقييد", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    
    elif query.data == "m2":
        await query.message.edit_text("**قائمة اوامر الاعدادات**\n━━━━━━━━━━━━\n• وضع (ترحيب، قوانين، رابط)\n• رؤية (المنشئين، الحماية، المجموعه)\n• تحميل (يوتيوب، تيك توك، ساوند)", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    
    elif query.data == "m3":
        await query.message.edit_text("**قائمة القفل والفتح**\n━━━━━━━━━━━━\n• قفل/فتح (الروابط، الصور، الفيديو)\n• تفعيل/تعطيل (الردود، الايدي، التسليه)", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))

    elif query.data == "m4":
        await query.message.edit_text("**قائمة اوامر التسليه**\n━━━━━━━━━━━━\n• رفع (هطف، خروف، زوجتي)\n• العاب، طلاق، زواج، اكتموه", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))

    elif query.data == "m5":
        await query.message.edit_text("**قائمة اوامر Dev**\n━━━━━━━━━━━━\n• اذاعة، تحديث، اعادة تشغيل\n• حظر عام، اضف رد عام", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))

    elif query.data == "m6":
        await query.message.edit_text("**قائمة الاوامر الخدميه**\n━━━━━━━━━━━━\n• قرآن، اذكار، زخرفة، ترجمة\n• نسب حب، افلام، اغاني، افتارات", 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))

app.run()

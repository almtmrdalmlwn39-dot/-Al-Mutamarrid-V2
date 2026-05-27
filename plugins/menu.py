from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# القائمة الرئيسية
@Client.on_message(filters.command("الاوامر", ""))
async def main_menu(client, message):
    text = "**- أهلاً بك عزيزي في قائمة الاوامر :**"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("1", callback_data="m1"), InlineKeyboardButton("2", callback_data="m2"), InlineKeyboardButton("3", callback_data="m3")],
        [InlineKeyboardButton("4", callback_data="m4"), InlineKeyboardButton("5", callback_data="m5"), InlineKeyboardButton("6", callback_data="m6")],
        [InlineKeyboardButton("🌐 اوامر Dev", callback_data="dev"), InlineKeyboardButton("🎮 اوامر التسليه", callback_data="games")],
        [InlineKeyboardButton("💖 اوامر خدميه", callback_data="services")],
        [InlineKeyboardButton("🛡️ القفل والفتح", callback_data="locks"), InlineKeyboardButton("🔗 التفعيل والتعطيل", callback_data="settings")]
    ])
    await message.reply_text(text, reply_markup=keyboard)

# معالجة ضغط الأزرار (النظام التفاعلي)
@Client.on_callback_query()
async def callback_handler(client, query):
    data = query.data
    
    # زر الرجوع للقائمة الرئيسية
    if data == "back":
        text = "**- أهلاً بك عزيزي في قائمة الاوامر :**"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("1", callback_data="m1"), InlineKeyboardButton("2", callback_data="m2"), InlineKeyboardButton("3", callback_data="m3")],
            [InlineKeyboardButton("4", callback_data="m4"), InlineKeyboardButton("5", callback_data="m5"), InlineKeyboardButton("6", callback_data="m6")],
            [InlineKeyboardButton("🌐 اوامر Dev", callback_data="dev"), InlineKeyboardButton("🎮 اوامر التسليه", callback_data="games")],
            [InlineKeyboardButton("💖 اوامر خدميه", callback_data="services")],
            [InlineKeyboardButton("🛡️ القفل والفتح", callback_data="locks"), InlineKeyboardButton("🔗 التفعيل والتعطيل", callback_data="settings")]
        ])
        await query.message.edit_text(text, reply_markup=keyboard)
        return

    # معالجة الأزرار الأخرى
    if data == "m1":
        await query.message.edit_text("**قسم أوامر الأدمنية:**\n\n• طرد - كتم - مسح", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    
    elif data == "locks":
        await query.message.edit_text("**قسم القفل والفتح:**\n\n• قفل السب\n• قفل الروابط\n• قفل الصور", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
        
    elif data == "settings":
        await query.message.edit_text("**قسم التفعيل والتعطيل:**\n\n• تفعيل الترحيب\n• تعطيل الردود", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))

    # أضف باقي الأزرار بنفس الطريقة (m2, m3, dev, games, etc...)

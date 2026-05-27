from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 1. القائمة الرئيسية
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

# 2. معالجة ضغط الأزرار (النظام التفاعلي)
@Client.on_callback_query()
async def callback_handler(client, query):
    data = query.data
    
    # القائمة الأساسية للرجوع
    main_kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("1", callback_data="m1"), InlineKeyboardButton("2", callback_data="m2"), InlineKeyboardButton("3", callback_data="m3")],
        [InlineKeyboardButton("4", callback_data="m4"), InlineKeyboardButton("5", callback_data="m5"), InlineKeyboardButton("6", callback_data="m6")],
        [InlineKeyboardButton("🌐 اوامر Dev", callback_data="dev"), InlineKeyboardButton("🎮 اوامر التسليه", callback_data="games")],
        [InlineKeyboardButton("💖 اوامر خدميه", callback_data="services")],
        [InlineKeyboardButton("🛡️ القفل والفتح", callback_data="locks"), InlineKeyboardButton("🔗 التفعيل والتعطيل", callback_data="settings")]
    ])

    if data == "back":
        await query.message.edit_text("**- أهلاً بك عزيزي في قائمة الاوامر :**", reply_markup=main_kb)
        return

    # محتوى الأزرار (مقسم حسب الرقم)
    if data == "m1":
        await query.message.edit_text("**- قائمة اوامر الادمنية :\n━━━━━━━━━━━━**\n• رفع وتنزيل الرتب\n• مسح الكل / المنشئين / الادمنية\n• الطرد / الحظر / الكتم\n━━━━━━━━━━━━", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    
    elif data == "m2":
        await query.message.edit_text("**- قائمة أوامر الإعدادات :\n━━━━━━━━━━━━**\n• ضبط الترحيب\n• ضبط القوانين\n• تفعيل/تعطيل الميزات\n━━━━━━━━━━━━", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
        
    elif data == "m3":
        await query.message.edit_text("**- قائمة أوامر القفل والفتح :\n━━━━━━━━━━━━**\n• قفل الصور / الروابط / التوجيه\n• فتح جميع الميزات\n━━━━━━━━━━━━", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))

    elif data == "m4":
        await query.message.edit_text("**- قائمة التسلية :\n━━━━━━━━━━━━**\n• العاب / ترفيه / نكت\n━━━━━━━━━━━━", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))

    elif data == "m5":
        await query.message.edit_text("**- أوامر المطور (Dev) :\n━━━━━━━━━━━━**\n• إذاعة للكل\n• تحديث السورس\n━━━━━━━━━━━━", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))

    elif data == "m6":
        await query.message.edit_text("**- الأوامر الخدمية :\n━━━━━━━━━━━━**\n• كشف الآيدي / معلومات المجموعة\n━━━━━━━━━━━━", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))

    elif data == "locks":
        await query.message.edit_text("**- قسم القفل الشامل**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    
    elif data == "settings":
        await query.message.edit_text("**- قسم التفعيل والتعطيل**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))

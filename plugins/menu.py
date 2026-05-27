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
    
    # تعريف القائمة الرئيسية للرجوع إليها
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

    # الأقسام المضافة (الآن كل زر له وظيفة)
    if data == "m1":
        await query.message.edit_text("**قسم أوامر الأدمنية (1):**\n\n• رفع وتنزيل الرتب\n• مسح الرسائل والمنشئين\n• الطرد والحظر والكتم", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "m2":
        await query.message.edit_text("**قسم أوامر الإعدادات (2):**\n\n• ضبط الترحيب\n• وضع قوانين المجموعة\n• تفعيل/تعطيل الميزات", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "m3":
        await query.message.edit_text("**قسم أوامر القفل والفتح (3):**\n\n• التحكم الكامل في قفل كل شيء (روابط، صور، سب)", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "m4":
        await query.message.edit_text("**قسم التسلية (4):**\n\n• ألعاب ترفيهية\n• مسابقات ونكت", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "m5":
        await query.message.edit_text("**قسم أوامر Dev (5):**\n\n• التحكم الخاص بالمطور\n• تحديث البوت/إذاعة", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "m6":
        await query.message.edit_text("**قسم الأوامر الخدمية (6):**\n\n• معلومات الآيدي\n• كشف الطقس", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    
    # الأزرار السفلية
    elif data == "locks":
        await query.message.edit_text("**قسم القفل والفتح الشامل:**\n\n• تحكم كامل في الحماية", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "settings":
        await query.message.edit_text("**قسم التفعيل والتعطيل:**\n\n• تفعيل/تعطيل الأذكار، المنشن، إلخ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "dev":
        await query.message.edit_text("**أوامر المطور Dev**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "games":
        await query.message.edit_text("**قسم التسلية الممتع**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))
    elif data == "services":
        await query.message.edit_text("**قسم الخدمات**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]]))

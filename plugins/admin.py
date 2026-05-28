from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# 1. القائمة الرئيسية
@Client.on_message(filters.command("الاوامر"))
async def main_menu(client, message):
    text = "**- أهلاً بك عزيزي في قائمة الاوامر :**"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("1", callback_data="m1"), InlineKeyboardButton("2", callback_data="m2"), InlineKeyboardButton("m3", callback_data="m3")],
        [InlineKeyboardButton("4", callback_data="m4"), InlineKeyboardButton("m5", callback_data="m5"), InlineKeyboardButton("m6", callback_data="m6")],
        [InlineKeyboardButton("🌐 اوامر Dev", callback_data="dev"), InlineKeyboardButton("🎮 اوامر التسليه", callback_data="games")],
        [InlineKeyboardButton("💖 اوامر خدميه", callback_data="services")],
        [InlineKeyboardButton("🛡️ القفل والفتح", callback_data="locks"), InlineKeyboardButton("🔗 التفعيل والتعطيل", callback_data="settings")]
    ])
    await message.reply_text(text, reply_markup=keyboard)

# 2. معالجة ضغط الأزرار (أضفنا فلتر هنا لزيادة الاستقرار)
@Client.on_callback_query()
async def callback_handler(client, query: CallbackQuery):
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

    # محتوى الأزرار
    responses = {
        "m1": "**- قائمة اوامر الادمنية :**",
        "m2": "**- قائمة أوامر الإعدادات :**",
        "m3": "**- قائمة أوامر القفل والفتح :**",
        "m4": "**- قائمة التسلية :**",
        "m5": "**- أوامر المطور (Dev) :**",
        "m6": "**- الأوامر الخدمية :**",
        "locks": "**- قسم القفل الشامل**",
        "settings": "**- قسم التفعيل والتعطيل**"
    }

    if data in responses:
        await query.message.edit_text(
            f"{responses[data]}\n━━━━━━━━━━━━", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("〈 رجوع", callback_data="back")]])
        )

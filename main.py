import os
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ChatMemberStatus

# --- سيرفر وهمي لمنع توقف ريندر ---
flask_app = Flask('')
@flask_app.route('/')
def home(): return "البوت يعمل!"
def run(): flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive(): Thread(target=run).start()

# --- بيانات البوت ---
API_ID = 26588241
API_HASH = "b90956461a510523097f48030999554b"
BOT_TOKEN = "7295980036:AAGR8wQYmX_uS_4-YF2D6tQpB2V_m_e-S_A"
SUDO_USERS = [7447817025, 6467728995] 

app = Client("almtmrd_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- دالة التحقق من الأدمن ---
async def is_admin(client, chat_id, user_id):
    if user_id in SUDO_USERS: return True
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

MENU_TEXT = "**- أهلاً بك عزيزي في قائمة الاوامر :**\n━━━━━━━━━━━━"
START_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("م1", callback_data="m1"), InlineKeyboardButton("م2", callback_data="m2"), InlineKeyboardButton("م3", callback_data="m3")],
    [InlineKeyboardButton("م4", callback_data="m4"), InlineKeyboardButton("م5", callback_data="m5"), InlineKeyboardButton("م6", callback_data="m6")],
    [InlineKeyboardButton("• قـناة الـسورس •", url="https://t.me/A0_07")]
])

@app.on_message(filters.command(["start", "الاوامر"]))
async def start(client, message):
    await message.reply_text(MENU_TEXT, reply_markup=START_BUTTONS)

@app.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    
    if data == "main":
        await query.message.edit_text(MENU_TEXT, reply_markup=START_BUTTONS)
        return

    # حماية الأقسام الحساسة
    if data in ["m1", "m2", "m3", "m5"]:
        if not await is_admin(client, chat_id, user_id):
            return await query.answer("⚠️ هذا القسم للمشرفين فقط!", show_alert=True)

    if data == "m1":
        await query.message.edit_text("**قسم الإدمنية:**\n• طرد / حظر / كتم", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    elif data == "m2":
        await query.message.edit_text("**قسم الإعدادات:**\n• ترحيب / قوانين", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    elif data == "m3":
        await query.message.edit_text("**قسم القفل والفتح:**\n• التحكم بالحماية", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    elif data == "m4":
        await query.message.edit_text("**قسم التسلية:**\n• ألعاب / نكت", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    elif data == "m5":
        await query.message.edit_text("**قسم المطور:**\n• إذاعة / تحديث", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))
    elif data == "m6":
        await query.message.edit_text("**قسم الخدمات:**\n• آيدي / معلومات", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="main")]]))

if __name__ == "__main__":
    keep_alive()
    app.run()

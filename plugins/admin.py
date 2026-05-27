from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from config import SUDO_USERS, CHANNEL_LINK

# مخازن البيانات المؤقتة
photo_locked_chats = []
links_locked_chats = []
forward_locked_chats = []
spam_protection = {} # لحماية التكرار

# --- 1. التحقق من الصلاحيات ---
async def is_admin(client, message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    return user.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER] or message.from_user.id in SUDO_USERS

# --- 2. أوامر التحكم الشاملة ---
@Client.on_message(filters.command(["قفل الصور", "فتح الصور", "قفل الروابط", "فتح الروابط", "قفل التوجيه", "فتح التوجيه", "قفل", "فتح"]) & filters.group)
async def admin_control(client, message):
    if not await is_admin(client, message):
        return await message.reply_text("⚠️ **هذا الأمر للمشرفين أو للمتمرد فقط!**")

    cmd = message.command[0]
    cid = message.chat.id

    if cmd == "قفل الصور":
        if cid not in photo_locked_chats: photo_locked_chats.append(cid)
        await message.reply_text("🚫 **تم قفل صور الآيدي.**")
    
    elif cmd == "فتح الصور":
        if cid in photo_locked_chats: photo_locked_chats.remove(cid)
        await message.reply_text("✅ **تم فتح صور الآيدي.**")

    elif cmd == "قفل الروابط":
        if cid not in links_locked_chats: links_locked_chats.append(cid)
        await message.reply_text("🚫 **تم قفل الروابط والمعرفات.**")

    elif cmd == "فتح الروابط":
        if cid in links_locked_chats: links_locked_chats.remove(cid)
        await message.reply_text("✅ **تم فتح الروابط.**")

    elif cmd == "قفل التوجيه":
        if cid not in forward_locked_chats: forward_locked_chats.append(cid)
        await message.reply_text("🚫 **تم قفل التوجيه (Forward).**")

    elif cmd == "فتح التوجيه":
        if cid in forward_locked_chats: forward_locked_chats.remove(cid)
        await message.reply_text("✅ **تم فتح التوجيه.**")

# --- 3. أوامر الطرد والكتم والمسح ---
@Client.on_message(filters.command(["طرد", "كتم", "مسح"]) & filters.group)
async def kick_mute_logic(client, message):
    if not await is_admin(client, message): return
    
    if message.command[0] == "مسح" and message.reply_to_message:
        await message.reply_to_message.delete()
        await message.delete()
    
    elif message.command[0] == "طرد" and message.reply_to_message:
        await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply_text("👤 **تم الطرد بنجاح.**")

# --- 4. محرك الحماية التلقائي (الرادار) ---
@Client.on_message(filters.group & ~filters.me)
async def protection_radar(client, message):
    if not message.from_user or message.from_user.id in SUDO_USERS: return
    cid = message.chat.id

    # 1. حماية الروابط والمعرفات
    if cid in links_locked_chats:
        if any(x in message.text.lower() for x in ["t.me/", "http", "@"]):
            try: await message.delete()
            except: pass

    # 2. حماية التوجيه
    if cid in forward_locked_chats and message.forward_from_chat:
        try: await message.delete()
        except: pass

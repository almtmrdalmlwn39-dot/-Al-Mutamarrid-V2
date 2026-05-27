from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from config import SUDO_USERS, CHANNEL_LINK # استدعاء البيانات من config

# --- 1. ترحيب وحقوق المتمرد ---
@Client.on_message(filters.new_chat_members)
async def welcome_rebel(client, message):
    for member in message.new_chat_members:
        await message.reply_text(
            f"**• أهلاً بك يا {member.mention} في مجموعتنا! 🛡️**\n"
            f"**• البوت محمي بواسطة سورس المتمرد.**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• قـناة الـمتمرد •", url=CHANNEL_LINK)],
                [InlineKeyboardButton("• الـمطور •", url="https://t.me/A0_O7")]
            ])
        )

# --- 2. أوامر السيطرة (قفل، فتح، طرد، كتم، مسح) ---
@Client.on_message(filters.command(["قفل", "فتح", "طرد", "كتم", "مسح"]) & filters.group)
async def admin_logic(client, message):
    # التحقق هل المستخدم هو أحد المطورين أو مشرف
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    is_sudo = message.from_user.id in SUDO_USERS
    
    if user.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER] and not is_sudo:
        return await message.reply_text("⚠️ **هذا الأمر للمشرفين أو للمتمرد فقط!**")

    cmd = message.command[0]

    if cmd == "قفل":
        await client.set_chat_permissions(message.chat.id, ChatPermissions(can_send_messages=False))
        await message.reply_text("🚫 **تم قفل الدردشة بحماية المتمرد.**")
    
    elif cmd == "فتح":
        await client.set_chat_permissions(message.chat.id, ChatPermissions(can_send_messages=True))
        await message.reply_text("✅ **تم فتح الدردشة.. انطلقوا!**")

    elif cmd == "مسح":
        if message.reply_to_message:
            await message.delete()
            await message.reply_to_message.delete()
        else:
            await message.reply_text("⚠️ **رد على الرسالة التي تريد مسحها.**")

    elif cmd == "طرد" and message.reply_to_message:
        await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply_text(f"👤 **تم طرد العضو بنجاح.**")

    elif cmd == "كتم" and message.reply_to_message:
        await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(can_send_messages=False))
        await message.reply_text(f"🔇 **تم كتم العضو.**")

# --- 3. نظام الإذاعة (للمطورين فقط) ---
@Client.on_message(filters.command("اذاعة") & filters.user(SUDO_USERS))
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply_text("**⚠️ رد على الرسالة (نص/صورة) لنشرها.**")
    
    msg = message.reply_to_message
    sent = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [ChatMemberStatus.GROUP, ChatMemberStatus.SUPERGROUP]:
            try:
                await msg.copy(dialog.chat.id)
                sent += 1
            except: pass
    await message.reply_text(f"**✅ تم نشر الإذاعة في {sent} مجموعة.**")

# --- 4. الحماية التلقائية (منع الروابط والمعرفات) ---
@Client.on_message(filters.group & ~filters.me)
async def auto_protection(client, message):
    # استثناء المطورين من الحذف
    if message.from_user and message.from_user.id in SUDO_USERS:
        return 

    if message.text and ("t.me/" in message.text or "http" in message.text or "@" in message.text):
        try:
            await message.delete()
        except: pass

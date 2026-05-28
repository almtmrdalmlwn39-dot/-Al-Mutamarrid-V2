from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus

@Client.on_message(filters.command("تاك", "") & filters.group)
async def tag_all(client, message):
    # التحقق من الصلاحيات (مع حماية بسيطة)
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return await message.reply_text("⚠️ **هذا الأمر للمشرفين فقط!**")
    except:
        return

    text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "يا شباب، المتمرد يريدكم!"
    
    tags = ""
    # جلب الأعضاء مع تحديد حد أقصى للحماية من الانهيار
    async for member in client.get_chat_members(message.chat.id, limit=200):
        if not member.user.is_bot:
            tags += f"[{member.user.first_name}](tg://user?id={member.user.id}) "
            if len(tags) > 3000:
                await message.reply_text(f"{text}\n\n{tags}")
                tags = ""
                await asyncio.sleep(2) # تأخير بسيط للحماية من الحظر
    
    if tags:
        await message.reply_text(f"{text}\n\n{tags}")

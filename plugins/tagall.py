from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus

# أمر التاكر (تاك للكل)
@Client.on_message(filters.command("تاك", "") & filters.group)
async def tag_all(client, message):
    # التحقق من صلاحيات المستخدم (لا يستخدمه إلا الأدمن)
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply_text("⚠️ **هذا الأمر للمشرفين فقط!**")

    # تحديد النص المكتوب مع الأمر
    text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "يا شباب، المتمرد يريدكم!"
    
    tags = ""
    async for member in client.get_chat_members(message.chat.id):
        if not member.user.is_bot:
            tags += f"[{member.user.first_name}](tg://user?id={member.user.id}) "
            # إرسال التاك على دفعات لتجنب الحظر
            if len(tags) > 4000:
                await message.reply_text(tags)
                tags = ""
    
    if tags:
        await message.reply_text(f"{text}\n\n{tags}")

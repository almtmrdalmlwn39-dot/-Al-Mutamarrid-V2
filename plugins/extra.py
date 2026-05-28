from pyrogram import Client, filters

# حذفنا استيراد config.py لتجنب الخطأ
# 1. الترحيب التلقائي ...
@Client.on_message(filters.new_chat_members & filters.group)
async def welcome(client, message):
    for new_user in message.new_chat_members:
        await message.reply_text(f"**أهلاً بك يا {new_user.mention} في مجموعتنا! 💖\nنورت المكان يا بطل.**")

# 2. رد المطور
@Client.on_message(filters.command("سورس"))
async def source_info(client, message):
    await message.reply_text("**- سورس المتمرد V2 🛰️🔥\n\n- بوت حماية متطور ومخصص للأدمنة.**")

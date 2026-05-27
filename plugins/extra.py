from pyrogram import Client, filters
from config import SUDO_USERS # التأكد من استيراد قائمة المطورين

# 1. الترحيب التلقائي بالأعضاء الجدد
@Client.on_message(filters.new_chat_members & filters.group)
async def welcome(client, message):
    for new_user in message.new_chat_members:
        await message.reply_text(
            f"**أهلاً بك يا {new_user.mention} في مجموعتنا! 💖\nنورت المكان يا بطل.**"
        )

# 2. رد المطور (حقوق السورس)
@Client.on_message(filters.command("سورس", ""))
async def source_info(client, message):
    await message.reply_text(
        "**- سورس المتمرد V2 🛰️🔥\n\n- بوت حماية متطور ومخصص للأدمنة.\n- برمجة وإعداد: [المتمرد]**"
    )

# 3. ردود ذكية (اختياري)
@Client.on_message(filters.regex("هلا|اهلين|سلام"), group=1)
async def greet_reply(client, message):
    await message.reply_text("أهلاً بك يا غالي! كيف يمكنني مساعدتك؟ 😊")

# 4. معرفة آيدي المجموعة
@Client.on_message(filters.command("الآيدي", ""))
async def get_id(client, message):
    await message.reply_text(f"**- آيدي المجموعة هو :** `{message.chat.id}`")

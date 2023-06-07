import asyncio
import random
from NibiMusic.config import BOT_USERNAME, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


NIBI_IMG = (
"https://graph.org/file/c2f110353910f1a166016.jpg",
"https://graph.org/file/c2f110353910f1a166016.jpg",
"https://graph.org/file/c2f110353910f1a166016.jpg",
"https://graph.org/file/c2f110353910f1a166016.jpg",
"https://graph.org/file/c2f110353910f1a166016.jpg",
"https://graph.org/file/c2f110353910f1a166016.jpg",
"https://graph.org/file/c2f110353910f1a166016.jpg",

)





START_TEXT = """
ʜɪ ɢᴜʏꜱ, ɪ ᴀᴍ ᴀʀɪᴀ x ᴍᴜsɪᴄ ᴀ ᴠᴇʀʏ ʜɪɢʜʟʏ ᴀ.ɪ ᴀᴅᴠᴀɴᴄᴇᴅ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ʙᴏᴛ.
ɪ' ᴍ ᴠᴇʀʏ ғᴀꜱᴛ ᴀɴᴅ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ !
"""

    
   

@Client.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(NIBI_IMG),
        caption=(START_TEXT),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/AriaXMusic_bot?startgroup=true")
        ],
        [
            InlineKeyboardButton("🍂 sᴜᴘᴘᴏʀᴛ", url="https://t.me/lovingfriendsforever"),
            InlineKeyboardButton("🌾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Dil_se_dil_tak_01")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/MrKhunii"),
        ]
   
     ]
  ),
)
    
    
@Client.on_message(filters.command(["repo", "source"]))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c2f110353910f1a166016.jpg",
        caption=f"""ʜᴇʀᴇ ɪs ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ғᴏʀᴋ ᴀɴᴅ ɢɪᴠᴇ sᴛᴀʀs ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://t.me/MrKhunii"
                    )
                ]
            ]
        ),
    )

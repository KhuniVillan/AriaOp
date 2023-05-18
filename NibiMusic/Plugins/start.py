import asyncio
import random
from NibiMusic.config import BOT_USERNAME, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


NIBI_IMG = (
"https://graph.org/file/92484a4578afe8348ed74.jpg",
"https://graph.org/file/92484a4578afe8348ed74.jpg",
"https://graph.org/file/92484a4578afe8348ed74.jpg",
"https://graph.org/file/92484a4578afe8348ed74.jpg",
"https://graph.org/file/92484a4578afe8348ed74.jpg",
"https://graph.org/file/92484a4578afe8348ed74.jpg",
"https://graph.org/file/92484a4578afe8348ed74.jpg",

)





START_TEXT = """
ʜɪ ɢᴜʏꜱ, ɪ ᴀᴍ ᴠᴇʀʏ ʜɪɢʜʟʏ ᴀ.ɪ ᴀᴅᴠᴀɴᴄᴇᴅ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ʙᴏᴛ.
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
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/Mistyopmusic_bot?startgroup=true")
        ],
        [
            InlineKeyboardButton("🍂 sᴜᴘᴘᴏʀᴛ", url="https://t.me/best_friends_chatting_grup"),
            InlineKeyboardButton("🌾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/mistyamraj_ki_kahani")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/brahmaan_sher"),
        ]
   
     ]
  ),
)
    
    
@Client.on_message(filters.command(["repo", "source"]))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/56557bd94afbe895ae483.jpg",
        caption=f"""ʜᴇʀᴇ ɪs ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ғᴏʀᴋ ᴀɴᴅ ɢɪᴠᴇ sᴛᴀʀs ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/TheFunkyFox/NibiMusic"
                    )
                ]
            ]
        ),
    )

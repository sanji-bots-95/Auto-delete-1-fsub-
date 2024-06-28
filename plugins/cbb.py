# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ 𝐁ʏ : <a href='https://t.me/Straw_Hat_Bots'>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ ꭙ 𝐁ᴏᴛs</a>\n○ 𝐁ᴏᴛ 𝐔ᴘᴅᴀᴛᴇs : <a href='https://t.me/Straw_Hat_Bots'>𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ</a>\n○ 𝐁ᴏᴛ 𝐒ᴜᴘᴘᴏʀᴛ : <a href='https://t.me/Straw_hat_support'>𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀᴛ : <a href='https://t.me/+BSL2tOp6BGE2MGU1'>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ 𝐆ʀᴏᴜᴘ </a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ Cʟᴏsᴇ", callback_data = "close")
                        
InlineKeyboardButton('🍁 Dᴇᴠᴇʟᴏᴘᴇʀs', url='https://t.me/Straw_Hat_Bots')                        
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, ForceReply
from pyrogram import Client, filters, enums
from bot import Bot
import asyncio



#############reply any massege from a group
##   (filters.group(coustom chat.id) & filters.text(eg - hi) & filters.incoming)
@Client.on_message(filters.group & filters.text & filters.incoming)
async def give_filter(client, message):
    button = [[InlineKeyboardButton(text="ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ", url=f"https://t.me/alexa_search_bot")]]
    await message.reply_text("<b>MESSAGE RESIVED</b>", reply_markup=InlineKeyboardMarkup(button))

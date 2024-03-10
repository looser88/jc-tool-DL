

from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, ForceReply
from pyrogram import Client, filters, enums
from bot import Bot


@Client.on_message(filters.group & filters.text & filters.incoming)
async def give_filter(client, message):
    button = [[InlineKeyboardButton(text="ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ", url=f"https://t.me/alexa_search_bot")]]
    await message.reply_text("<b>MESSAGE RESIVED</b>", reply_markup=InlineKeyboardMarkup(button))
    
    
######## reply_markup=ForceReply (NOT SOLVED)
@Client.on_message(filters.private & filters.command(["create_channel"]))
async def give_filter(Client, message):
    id = message.reply_to_message_id
    mp = await message.reply_text(f"**𝙿𝚕𝚎𝚊𝚜𝚎  𝙴𝚗𝚝𝚎𝚛  𝚃𝚑𝚎  𝙽𝚎𝚠  𝙵𝚒𝚕𝚎𝚗𝚊𝚖𝚎", quote=True, reply_to_message_id = id, reply_markup=ForceReply(True))
    print(mp)
    #await Client.create_channel("Channel Title", "Channel Description")
    
    
######## to use reply_markup=ReplyKeyboardMarkup , KeyboardButton
@Client.on_message(filters.private & filters.command(["ReplyKm"]))
async def give_filter(Client, message):
    id = message.reply_to_message_id
    button = [[KeyboardButton(text="ᴄᴏɴᴛᴀᴄᴛ", request_contact=True),
              KeyboardButton(text="ᴄᴏɴᴛᴀᴄᴛ", request_contact=True)]]
    mp = await message.reply_text(f"**𝙿𝚕𝚎𝚊𝚜𝚎  𝙴𝚗𝚝𝚎𝚛  𝚃𝚑𝚎  𝙽𝚎𝚠  𝙵𝚒𝚕𝚎𝚗𝚊𝚖𝚎", quote=True, reply_markup=ReplyKeyboardMarkup(button))

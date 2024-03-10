from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, ForceReply
from pyrogram import Client, filters, enums
from bot import Bot
import asyncio



############## RUN MULPLE BUTTTUN FROM LIST
SPELL_IMG ="https://graph.org/file/ead67f78d85f79338bdac.jpg"
movielist =["A","B","C","D","E","F"]
@Bot.on_message(filters.private & filters.command(["blkbtn"]))
async def echodot(bot, update):
    btn = [[InlineKeyboardButton(text=k, callback_data=mv,)]
            for mv in movielist  
          ]
    # btn.append([InlineKeyboardButton(text="Close", callback_data=f'spol#{reqstr1}#close_spellcheck')])
    await update.reply_photo(photo=(SPELL_IMG), caption="hello", reply_markup=InlineKeyboardMarkup(btn))
    
    
######## reply_markup=ForceReply TAKE SAME REPLY 
@Client.on_message(filters.private & filters.command(["take_reply"]))
async def take_ans(Client, message):
    f_msg = await Client.ask(text = "**𝙿𝚕𝚎𝚊𝚜𝚎 𝙴𝚗𝚝𝚎𝚛 𝙽𝚊𝚖𝚎**", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
    f_msg_txt = f_msg.text
    await Client.send_message(message.chat.id, f_msg_txt)
    
          ##################  ANOTHER METHOD ####################

@Client.on_message(filters.private & filters.command(["take_reply"]))
async def take_ans(Client, message):
    id = message.reply_to_message_id
    mp = await message.reply_text(f"**𝙿𝚕𝚎𝚊𝚜𝚎 𝙴𝚗𝚝𝚎𝚛 𝙽𝚊𝚖𝚎**", quote=True, reply_to_message_id = id, reply_markup=ForceReply(True))

@Bot.on_message(filters.private & filters.reply & filters.text)
async def cus_name(bot, message):
    mp_msg_txt = message.id
    await message.reply_text(text = mp_msg_txt)
    if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        mp_msg_txt = str(message.id)
        await message.reply_text(text = mp_msg_txt)   
    else:
        print('No media present')


######## to use reply_markup=ReplyKeyboardMarkup , KeyboardButton
@Client.on_message(filters.private & filters.command(["ReplyKm"]))
async def give_filter(Client, message):
    id = message.reply_to_message_id
    button = [[KeyboardButton(text="ᴄᴏɴᴛᴀᴄᴛ", request_contact=True),
              KeyboardButton(text="ᴄᴏɴᴛᴀᴄᴛ", request_contact=True)]]
    mp = await message.reply_text(f"**𝙿𝚕𝚎𝚊𝚜𝚎  𝙴𝚗𝚝𝚎𝚛  𝚃𝚑𝚎  𝙽𝚎𝚠  𝙵𝚒𝚕𝚎𝚗𝚊𝚖𝚎", quote=True, reply_markup=ReplyKeyboardMarkup(button))

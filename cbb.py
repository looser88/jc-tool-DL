#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
import pytz 
import time
from config import OWNER_ID
from datetime import datetime, timedelta
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

global DATEDAY
DATEDAY = []

async def timeout(timeout):
    start_time = time.time()
    while time.time() < start_time + timeout:
      DATEDAY.clear()
    return 
 
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    india = pytz.timezone("Asia/Kolkata") #for Indian date and timings 
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @CodeXBotz\n○ Support Group : @CodeXBotzSupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
    elif data == "ystdy":
        DATEDAY.clear()
        ye = datetime.now(india)-timedelta(1)
        DATEDAY.append(str(ye.strftime("%d ⚡ %m ⚡ %Y")))
        await query.message.edit_text(text = f"<b>Date change to :'{DATEDAY[-1]}'</b>", reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]])) # A query msg edit for (in plugins->channel post->line 21) ==> this return a date from previous date stored in DATEDAY variable (line 10)
        timeout(10)
    elif data == "tdy":
        DATEDAY.clear()
        tda = datetime.now(india)
        DATEDAY.append(str(tda.strftime("%d ⚡ %m ⚡ %Y")))
        timeout(10)
        await query.message.edit_text(text = f"<b>Date change to :'{DATEDAY[-1]}'</b>", reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))
        
    elif data == "tmr":
        DATEDAY.clear()
        tm = datetime.now(india)+timedelta(1)
        DATEDAY.append(str(tm.strftime("%d ⚡ %m ⚡ %Y")))
        timeout(10)
        await query.message.edit_text(text = f"<b>Date change to :'{DATEDAY[-1]}'</b>", reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))
        
    else:
        pass

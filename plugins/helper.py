# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """
Hi 👋 {}!
        
__A Simple PDsik Uploader Bot. It Can Upload Link To PDisk.
Send Me Any Direct Link Or YouTube or Video Link I Will Upload To PDisk And Give Direct Pdisk Link

> Support Custom Thumbnail
> Support Custom Tittle Name

Read /help Carefully & Do Follow All Given Instruction... __

✪ » **Create Your Own bot for Personal use** ⤵️
"""

HELP = """
**How to Use Me...**

⦿ Its Easy to Use me 
✪ » Send me Any Direct Link or YouTube Link
✪ » i will upload to PDisk & Give Link

➠ If you want Upload Telegram file,Videos to PDisk
✪ » First Send any File to @Link4Filesbot to generate Direct Link
✪ » Copy Generated Link and Paste here...
✪ » Violaaaa.... Done

➠ If You Want add Custom Tittle & Thumbnail Follow These Steps

✪ » link | Title

Or

✪ » Video link | Title | Thumbnail link
        (generate Thumbnail Link with Telegraph bot[@TGraphXbot])

NOTE:
➢ Do Not Spam, Send Link One By One, 
➢ The Video File is Available on Your LINK ones Upload Process is Complete, it Take Time Depend on Your File Size & My Server Upload Speed
So,be Patient 😴😴😴😴"""

# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🍿 Daddy 🍿', url='https://t.me/AnnihilusOP')
        ],[
        InlineKeyboardButton('Channel', url='https://telegram.me/MoviZenX'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )



@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )


@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()

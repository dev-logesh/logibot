from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from logibot import pbot, START_IMG, SUPPORT_CHAT


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""✨ **Hey I'm LOGI ROBOT** 

**Owner : [꧁۝༒LOGI꧂](https://t.me/cl_me_logesh)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

**Click on Button Bellow For More**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="꧁SOURCE۝꧂", url=f"https://github.com/LOGI-LAB/logibot"), 
                    InlineKeyboardButton(
                        "꧁۝༒𝑺𝒖𝒑𝒑𝒐𝒓𝒕꧂", url=f"https://t.me/{SUPPORT_CHAT}")
                ]
            ]
        )
    )

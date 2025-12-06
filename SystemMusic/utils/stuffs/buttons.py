from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/+xfr6-ZOTaZVmODU1"),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/Iamistkhar")
    ],
    [
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG"),
        InlineKeyboardButton("˹ ʙᴧᴄᴋ ˼", callback_data=f"settingsback_helper")
    ]
    ]
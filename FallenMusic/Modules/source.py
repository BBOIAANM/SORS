import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["المبرمج","السورس","المطور","يا سورس"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/46acb5dfcebe609eb25eb.mp4",
        caption=f"""᭙ᥱᥣᥴ᥆ꪔᥱ ƚ᥆ ᥉᥆ᥙᖇᥴᥱ ɦ᥆ᖇ᥉ᥱ

ƚɦᥱ ხᥱ᥉ƚ ᥉᥆ᥙᖇᥴᥱ ᥆ꪀ ƚᥱᥣᥱgᖇᥲꪔ

ƒ᥆ᥣᥣ᥆᭙ ƚɦᥱ ხᥙƚƚ᥆ꪀ᥉ ხᥱᥣ᥆᭙""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❪ يوزر المطور |✅ ❫", url=f"https://t.me/F_F_F_V"),
                ],[
                    InlineKeyboardButton(
                        "❪ قناة المطور |🥱 ❫", url=f"https://t.me/BV_YQ"), 
                    InlineKeyboardButton(
                        "❪ حساب المطور 2، |🌍  ❫", url=f"https://t.me/CBSNAM"),
                ],[
                    InlineKeyboardButton(
                        "❪ كروب الدعم | ✅ ❫", url=f"https://t.me/naj_vab"), 
                 ],[
                   
                ],

            ]

        ),

    )

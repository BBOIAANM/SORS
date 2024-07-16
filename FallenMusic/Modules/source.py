import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from FallenMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from FallenMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["المبرمج","السورس","المطور","يا سورس"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/46acb5dfcebe609eb25eb.mp4",
        caption=f"""هلابيك وردة بسورس چافا ياحلو
• اذا تريد تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت

سورس جافا لصنع بوتات الميوزگ | ✅

تواصل معناا 👇""",
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

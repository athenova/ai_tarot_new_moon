import os
import telebot
from openai import OpenAI
import ephem
from datetime import datetime

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
CHAT_ID = -1002374309134
#CHAT_ID = '@ai_tarot'

def job(sign, symbol, new_moon_date):
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - профессиональный таролог" },
            { "role": "user", "content": f"Составь таро-гороскоп на новолуние для знака '{sign}', используй смайлики, не пиши дату" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    text = f"""{symbol} **{sign}. Новолуние {new_moon_date.strftime('%d-%m-%Y')}**  {symbol}

{text}    
"""
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

today = datetime.now().date()
new_moon_date = ephem.next_new_moon(today).datetime().date()
job('Рыбы', symbol='♓', new_moon_date=new_moon_date)
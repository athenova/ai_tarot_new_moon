import os
import telebot
import schedule
import time
from datetime import datetime
from datetime import timedelta
from openai import OpenAI
import ephem

AI_TEXT_MODEL = 'gpt-4o-mini'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@ai_tarot'

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
    text = f"""{symbol} **{sign}. Новолуние {new_moon_date.strftime('%d-%m-%Y')}** {symbol}

{text}    
"""
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

today = datetime.now().date()
new_moon_date = ephem.next_new_moon(today).datetime().date()
check_date = today + timedelta(days=2)

if new_moon_date == check_date:
    schedule.every().day.at("14:00",'Europe/Moscow').do(job, sign="Рыбы", symbol='♓', new_moon_date=new_moon_date)
    schedule.every().day.at("14:01",'Europe/Moscow').do(job, sign="Овен", symbol='♈', new_moon_date=new_moon_date)
    schedule.every().day.at("14:02",'Europe/Moscow').do(job, sign="Телец", symbol='♉', new_moon_date=new_moon_date)
    schedule.every().day.at("14:03",'Europe/Moscow').do(job, sign="Близнецы", symbol='♊', new_moon_date=new_moon_date)
    schedule.every().day.at("14:04",'Europe/Moscow').do(job, sign="Рак", symbol='♋', new_moon_date=new_moon_date)
    schedule.every().day.at("14:05",'Europe/Moscow').do(job, sign="Лев", symbol='♌', new_moon_date=new_moon_date)
    schedule.every().day.at("14:06",'Europe/Moscow').do(job, sign="Дева", symbol='♍', new_moon_date=new_moon_date)
    schedule.every().day.at("14:07",'Europe/Moscow').do(job, sign="Весы", symbol='♎', new_moon_date=new_moon_date)
    schedule.every().day.at("14:08",'Europe/Moscow').do(job, sign="Скорпион", symbol='♏', new_moon_date=new_moon_date)
    schedule.every().day.at("14:09",'Europe/Moscow').do(job, sign="Стрелец", symbol='♐', new_moon_date=new_moon_date)
    schedule.every().day.at("14:10",'Europe/Moscow').do(job, sign="Козерог", symbol='♑', new_moon_date=new_moon_date)
    schedule.every().day.at("14:11",'Europe/Moscow').do(job, sign="Водолей", symbol='♒', new_moon_date=new_moon_date)

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)

import os
import telebot
import schedule
import time
from datetime import datetime
from datetime import timedelta
from openai import OpenAI
import ephem

AI_TEXT_MODEL = 'chatgpt-4o-latest'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@ai_tarot'

def job(sign, symbol, CHAT_ID=CHAT_ID):
    today = datetime.now().date()
    new_moon_date = ephem.next_new_moon(today).datetime()
    day = new_moon_date.strftime('%Y-%m-%d')
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - профессиональный таролог" },
            { "role": "user", "content": f"Составь таро-гороскоп на новолуние {day} для знака '{sign}', используй смайлики, не пиши дату" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    text = f"""{symbol} **{sign}. Новолуние {day}** {symbol}

{text}    
"""
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

if __name__ == '__main__':
    today = datetime.now().date()
    new_moon_date = ephem.next_new_moon(today).datetime().date()
    check_date = today + timedelta(days=2)

    if new_moon_date == check_date:
        schedule.every().day.at("14:00",'Europe/Moscow').do(job, sign="Рыбы", symbol='♓', CHAT_ID='@pisces_the')
        schedule.every().day.at("14:01",'Europe/Moscow').do(job, sign="Овен", symbol='♈', CHAT_ID='@aries_the')
        schedule.every().day.at("14:02",'Europe/Moscow').do(job, sign="Телец", symbol='♉')
        schedule.every().day.at("14:03",'Europe/Moscow').do(job, sign="Близнецы", symbol='♊', CHAT_ID='@gemini_the')
        schedule.every().day.at("14:04",'Europe/Moscow').do(job, sign="Рак", symbol='♋')
        schedule.every().day.at("14:05",'Europe/Moscow').do(job, sign="Лев", symbol='♌')
        schedule.every().day.at("14:06",'Europe/Moscow').do(job, sign="Дева", symbol='♍')
        schedule.every().day.at("14:07",'Europe/Moscow').do(job, sign="Весы", symbol='♎')
        schedule.every().day.at("14:08",'Europe/Moscow').do(job, sign="Скорпион", symbol='♏')
        schedule.every().day.at("14:09",'Europe/Moscow').do(job, sign="Стрелец", symbol='♐')
        schedule.every().day.at("14:10",'Europe/Moscow').do(job, sign="Козерог", symbol='♑', CHAT_ID='@capricorn_the')
        schedule.every().day.at("14:11",'Europe/Moscow').do(job, sign="Водолей", symbol='♒', CHAT_ID='@aquarius_the')

        fifteen_minutes = 15 * 60

        for i in range(fifteen_minutes):
            schedule.run_pending()
            time.sleep(1)

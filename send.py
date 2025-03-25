from project import *
import schedule
import time
import ephem
from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':
    today = datetime.now().date()
    new_moon_date = ephem.next_new_moon(today).datetime().date()
    check_date = today + timedelta(days=2)
    
    if new_moon_date == check_date:
        tg = ProjectTelegram()
        vk = ProjectVk()

        def job(type, chat_id=None, group_id=None):
            tg.send(type=type, chat_id=chat_id)
            if group_id is not None:
                vk.send(type=type, group_id=group_id, image_gen=False, text_gen=False)

        schedule.every().day.at("20:30",'Europe/Moscow').do(job, type="pisces", chat_id='@pisces_the', group_id='229837683')
        schedule.every().day.at("20:31",'Europe/Moscow').do(job, type="aries", chat_id='@aries_the', group_id='229837854')
        schedule.every().day.at("20:32",'Europe/Moscow').do(job, type="taurus", group_id='229860740')
        schedule.every().day.at("20:33",'Europe/Moscow').do(job, type="gemini", chat_id='@gemini_the', group_id='229837895')
        schedule.every().day.at("20:34",'Europe/Moscow').do(job, type="cancer", group_id='229860780')
        schedule.every().day.at("20:35",'Europe/Moscow').do(job, type="leo", group_id='229860665')
        schedule.every().day.at("20:36",'Europe/Moscow').do(job, type="virgo", group_id='229860810')
        schedule.every().day.at("20:37",'Europe/Moscow').do(job, type="libra", group_id='229860834')
        schedule.every().day.at("20:38",'Europe/Moscow').do(job, type="scorpio", group_id='229860866')
        schedule.every().day.at("20:39",'Europe/Moscow').do(job, type="sagittarius", group_id='229860894')
        schedule.every().day.at("20:40",'Europe/Moscow').do(job, type="capricorn", chat_id='@capricorn_the', group_id='229837876')
        schedule.every().day.at("20:41",'Europe/Moscow').do(job, type="aquarius", chat_id='@aquarius_the', group_id='229837930')

        fifteen_minutes = 15 * 60

        for i in range(fifteen_minutes):
            schedule.run_pending()
            time.sleep(1)


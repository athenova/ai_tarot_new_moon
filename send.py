from project import Project
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

        schedule.every().day.at("21:00",'Europe/Moscow').do(job, type="pisces", chat_id='@pisces_the', group_id='229837683')
        schedule.every().day.at("21:01",'Europe/Moscow').do(job, type="aries", chat_id='@aries_the', group_id='229837854')
        schedule.every().day.at("21:02",'Europe/Moscow').do(job, type="taurus")
        schedule.every().day.at("21:03",'Europe/Moscow').do(job, type="gemini", chat_id='@gemini_the', group_id='229837895')
        schedule.every().day.at("21:04",'Europe/Moscow').do(job, type="cancer")
        schedule.every().day.at("21:05",'Europe/Moscow').do(job, type="leo")
        schedule.every().day.at("21:06",'Europe/Moscow').do(job, type="virgo")
        schedule.every().day.at("21:07",'Europe/Moscow').do(job, type="libra")
        schedule.every().day.at("21:08",'Europe/Moscow').do(job, type="scorpio")
        schedule.every().day.at("21:09",'Europe/Moscow').do(job, type="sagittarius")
        schedule.every().day.at("21:10",'Europe/Moscow').do(job, type="capricorn", chat_id='@capricorn_the', group_id='229837876')
        schedule.every().day.at("21:11",'Europe/Moscow').do(job, type="aquarius", chat_id='@aquarius_the', group_id='229837930')

        fifteen_minutes = 15 * 60

        for i in range(fifteen_minutes):
            schedule.run_pending()
            time.sleep(1)


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
        p = Project()
        schedule.every().day.at("20:00",'Europe/Moscow').do(p.send, type="pisces", chat_id='@pisces_the')
        schedule.every().day.at("20:01",'Europe/Moscow').do(p.send, type="aries", chat_id='@aries_the')
        schedule.every().day.at("20:02",'Europe/Moscow').do(p.send, type="taurus")
        schedule.every().day.at("20:03",'Europe/Moscow').do(p.send, type="gemini", chat_id='@gemini_the')
        schedule.every().day.at("20:04",'Europe/Moscow').do(p.send, type="cancer")
        schedule.every().day.at("20:05",'Europe/Moscow').do(p.send, type="leo")
        schedule.every().day.at("20:06",'Europe/Moscow').do(p.send, type="virgo")
        schedule.every().day.at("20:07",'Europe/Moscow').do(p.send, type="libra")
        schedule.every().day.at("20:08",'Europe/Moscow').do(p.send, type="scorpio")
        schedule.every().day.at("20:09",'Europe/Moscow').do(p.send, type="sagittarius")
        schedule.every().day.at("20:10",'Europe/Moscow').do(p.send, type="capricorn", chat_id='@capricorn_the')
        schedule.every().day.at("20:11",'Europe/Moscow').do(p.send, type="aquarius", chat_id='@aquarius_the')

        fifteen_minutes = 15 * 60

        for i in range(fifteen_minutes):
            schedule.run_pending()
            time.sleep(1)

from simple_blogger import SimplestBlogger
from string import Template
from datetime import datetime
import ephem
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.VkSender import VkSender

class Project(SimplestBlogger):
    def _example_task_creator(self):
        prompt = Template(f"Составь таро-гороскоп на новолуние $$date для знака '$sign', используй смайликии, используй не более {self.topic_word_limit} слов")
        return [{ 
            "pisces_prompt": prompt.substitute(sign='Рыбы'),
            "aries_prompt": prompt.substitute(sign='Овен'),
            "taurus_prompt": prompt.substitute(sign='Телец'),
            "gemini_prompt": prompt.substitute(sign='Близнецы'),
            "cancer_prompt": prompt.substitute(sign='Рак'),
            "leo_prompt": prompt.substitute(sign='Лев'),
            "virgo_prompt": prompt.substitute(sign='Дева'),
            "libra_prompt": prompt.substitute(sign='Весы'),
            "scorpio_prompt": prompt.substitute(sign='Скорпион'),
            "sagittarius_prompt": prompt.substitute(sign='Стрелец'),
            "capricorn_prompt": prompt.substitute(sign='Козерог'),
            "aquarius_prompt": prompt.substitute(sign='Водолей'),
        }]
    
    def _preprocess_text_prompt(self, prompt):
        today = datetime.now().date()
        new_moon_date = ephem.next_new_moon(today).datetime()
        date = new_moon_date.strftime('%Y-%m-%d')
        return Template(prompt).substitute(date=date)
    
    def _system_prompt(self, _):
        return f"Ты - профессиональный таролог"
    
class ProjectTelegram(Project):
    def __init__(self, **kwargs):
        super().__init__(            
            reviewer=TelegramSender(),
            senders=[TelegramSender(channel_id='@ai_tarot')],
            **kwargs)
        
class ProjectVk(Project):
    def __init__(self, **kwargs):
        super().__init__(            
            reviewer=VkSender(group_id='229822833'),
            senders=[VkSender()],
            **kwargs)

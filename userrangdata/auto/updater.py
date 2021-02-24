from apscheduler.schedulers.background import BackgroundScheduler
from . import scrap


def start():
    scheduler = BackgroundScheduler()    
    scheduler.add_job(scrap.getinfo, "cron", hour='0', minute='57')
    scheduler.start()

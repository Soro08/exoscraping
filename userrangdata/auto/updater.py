from apscheduler.schedulers.background import BackgroundScheduler
from . import scrap


def start():
    scheduler = BackgroundScheduler()    
    scheduler.add_job(scrap.getinfo, "interval", seconds=15)
    scheduler.start()
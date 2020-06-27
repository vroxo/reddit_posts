from flask import Flask
from flask_apscheduler import APScheduler
from .commands import job_reddit_posts

__flask_scheduler = APScheduler()
scheduler = __flask_scheduler.scheduler


def init_app(app: Flask):
    __flask_scheduler.init_app(app)
    scheduler.add_job(job_reddit_posts, trigger='interval', minutes=10)
    scheduler.start()



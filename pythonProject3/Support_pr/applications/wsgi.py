"""
WSGI config for .

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
scheduler = BackgroundScheduler()
def scheduled_task():
    pass
trigger = DateTrigger(datetime.now())  # или используйте другой триггер
scheduler.add_job(scheduled_task, trigger)
scheduler.start()
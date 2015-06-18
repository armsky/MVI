__author__ = 'Hao Lin'

import sys
from celery import Celery
sys.path.append("../..")
import settings
import time

app = Celery('tasks',
             broker='amqp://localhost',
             backend='amqp',
             )

@app.task(name='utils.celery.tasks')
def add(x, y):
    time.sleep(3)
    print x+y
    return

# def download(ftp_handler, source_path, destination):

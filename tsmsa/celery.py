from __future__ import absolute_import
from celery import Celery, platforms
import os
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta


# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tsmsa.settings")

# 创建celery应用及配置

app = Celery('tsmsas', namespace='CELERY')

app.config_from_object('django.conf:settings')


# 如果在工程的应用中创建了tasks.py模块，那么Celery应用就会自动去检索创建的任务。比如你添加了一个任#务，在django中会实时地检索出来。
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



app.conf.update(
    CELERYBEAT_SCHEDULE={
        'sum-task': {
            'task': 'auth_admin.tasks.add',
            'schedule':  timedelta(seconds=20),
            'args': (5, 6)
        },
        'send-report': {
            'task': 'auth_admin.tasks.sub',
            'args': (5, 6),
            'schedule': timedelta(seconds=50),
        }
    }
)
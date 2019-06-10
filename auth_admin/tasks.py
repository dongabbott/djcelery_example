from __future__ import absolute_import
import time
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from tsmsa.celery import app


logger = get_task_logger('myapp')


@app.task
def send_message_email(mail_dict):
   logger.debug('开始给{}发送邮箱'.format(str(mail_dict)))
   send_mail(
      'abbott_test',  # 标题
      '你们干什么在',  # 内容
      'dongjie02@sunlands.com',  # 你的邮箱
      mail_dict,  # 收件人邮箱
      fail_silently=False,
   )


@app.task
def add(x, y):
    print("%d + %d = %d" % (x, y, x+y))
    return x + y


@app.task
def mul(x,y):
    print("%d * %d = %d" % (x, y, x*y))
    return x*y


@app.task
def sub(x,y):
    print("%d - %d = %d" % (x, y, x-y))
    return x - y
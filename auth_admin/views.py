from django.shortcuts import render, HttpResponse
import json

# Create your views here.
def add_handler(request):
   from .tasks import add, send_message_email

   send_message_email.delay(['dongjie02@sunlands.com'])
   res = {'code':200, 'message':'ok'}
   return HttpResponse(json.dumps(res))
from django.shortcuts import render
from asgiref.sync import async_to_sync
from tgbot.tasks import write_checked_schedule_db, write_schedule_db
from .webhook import proceed_update
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

async def home(request: HttpRequest):
    # await write_schedule_db()
    await write_checked_schedule_db()
    return HttpResponse('Hello world')

@csrf_exempt
def telegram(request: HttpRequest):
    # if request.method == 'post':
    try:
        async_to_sync(proceed_update)(request)
    except Exception as e:
        print(e)
    return HttpResponse()
    # else:
    #     return HttpResponse(status=403)
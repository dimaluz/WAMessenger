from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from . import wa_sender
from . import models
from .wa_components.wa_parser import post_webhook_parser
from .wa_components.db_query import select_message_by_id
from .wa_components.db_builder import (
    build_wa_message_deliverability, 
    build_wa_message_error, 
    build_wa_message_response,
)

def home_page(request):
    return HttpResponse('Home Page', status=200)

#                            Webhook receiver function

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = 'webhooktest'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)
        
    if request.method == 'POST':
        data = json.loads(request.body)
        print(150*'=')
        print('POST_WEBHOOK: ', data)
        print(150*'=')
        print('\n')
        parsed_webhook = post_webhook_parser(data)
        print(150*'=')
        print('PARSED_WEBHOOK: ', parsed_webhook)
        print(150*'=')
        campaign_id = select_message_by_id(parsed_webhook['wa_message_id'])
        
        if 'status' in parsed_webhook and parsed_webhook['status'] != 'failed':
            build_wa_message_deliverability(campaign_id, parsed_webhook)
        elif 'from' in parsed_webhook:
                build_wa_message_response(campaign_id, parsed_webhook)
        else:
            build_wa_message_error(campaign_id, parsed_webhook)
            
        return HttpResponse('success', status=200)



def send_message_test(request, message_id):
    message = models.WAMessage.objects.get(id=message_id)
    print("WAMessage: ", message)
    send = wa_sender.send_wa_msg('789060637290', message)
    print("MESSAGE WAS SENT AND NEW CAMPAIGN WAS CREATED: ", send)
    return HttpResponse('success', status=200)
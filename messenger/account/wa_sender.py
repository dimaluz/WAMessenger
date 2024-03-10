import json
import requests

from . import models
from .wa_components.wa_parser import get_webhook_parser
from .wa_components.db_builder import build_wa_message_campaign

TEMP_VERIFICATION_TOKEN = 'EAAFoIROj784BO4HnDuj8OenFxAqbZBehUH1a6xoF2MhMSe79Uzzq24RRWkZAg8WCanijoVhHeDpu4Tq8JZAoJwZCX72i7TuwRSHAeMuaas0GSXZBrywrN29pYTLe5KACSHxuGKe8f67LjaLPRuK9YN5eF0TXypktSpoyzq7ZBtbtmf2ZCRQptxOrcYCdZBM0Xtt4MjIpjS6NZBmrJMtegEBoZD'
#Phone number ID from Business Account
PHONE_NUMBER_ID = '186959564503397'

def send_wa_msg(phone_number, message):
    print('PHONE_NUMBER {0} MESSAGE_BODY {1}'.format(phone_number, message.message_body))
    WHATSAPP_URL = 'https://graph.facebook.com/v18.0/'+PHONE_NUMBER_ID+'/messages'
    header = {
        'Authorization': 'Bearer '+ TEMP_VERIFICATION_TOKEN,
    }
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type':"individual",
        'to': str(phone_number),
        'type': 'text',
        "text": {
            "body": message.message_body
       }
    }
    response = requests.post(WHATSAPP_URL, headers=header, json=data)
    wa_webhook = None
    while wa_webhook == None:
        wa_webhook = response.json()
        print(wa_webhook)
    parsed_webhook = get_webhook_parser(wa_webhook)
    response_from_builder = build_wa_message_campaign(message, parsed_webhook)
    return response_from_builder



def send_wa_image(phone_number, image_url, message=None):
    WHATSAPP_URL = 'https://graph.facebook.com/v17.0/'+PHONE_NUMBER_ID+'/messages'
    header = {
        'Authorization': 'Bearer '+ TEMP_VERIFICATION_TOKEN,
    }
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type':"individual",
        'to': str(phone_number),
        'type': 'image',
        "image": {
            "link": image_url,
            "caption": message
       }
    }
    response = requests.post(WHATSAPP_URL, headers=header, json=data)
    ans = response.json()
    return ans



def send_wa_audio(phone_number, audio_url):
    WHATSAPP_URL = 'https://graph.facebook.com/v17.0/'+PHONE_NUMBER_ID+'/messages'
    header = {
        'Authorization': 'Bearer '+ TEMP_VERIFICATION_TOKEN,
    }
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type':"individual",
        'to': str(phone_number),
        'type': 'audio',
        "audio": {
            "link": audio_url
       }
    }
    response = requests.post(WHATSAPP_URL, headers=header, json=data)
    ans = response.json()
    return ans


def send_wa_video(phone_number, video_url):
    WHATSAPP_URL = 'https://graph.facebook.com/v17.0/'+PHONE_NUMBER_ID+'/messages'
    header = {
        'Authorization': 'Bearer '+ TEMP_VERIFICATION_TOKEN,
    }
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type':"individual",
        'to': str(phone_number),
        'type': 'video',
        "video": {
            "link": video_url
       }
    }
    response = requests.post(WHATSAPP_URL, headers=header, json=data)
    ans = response.json()
    return ans


def send_wa_document(phone_number, document_url):
    WHATSAPP_URL = 'https://graph.facebook.com/v17.0/'+PHONE_NUMBER_ID+'/messages'
    header = {
        'Authorization': 'Bearer '+ TEMP_VERIFICATION_TOKEN,
    }
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type':"individual",
        'to': str(phone_number),
        'type': 'document',
        "document": {
            "link": document_url
       }
    }
    response = requests.post(WHATSAPP_URL, headers=header, json=data)
    ans = response.json()
    return ans


def send_wa_button(phone_number, title):
    WHATSAPP_URL = 'https://graph.facebook.com/v17.0/'+PHONE_NUMBER_ID+'/messages'
    header = {
        'Authorization': 'Bearer '+ TEMP_VERIFICATION_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        'messaging_product': 'whatsapp',
        'recipient_type':"individual",
        'to': str(phone_number),
        'type': 'interactive',
        "interactive": {
            "type":"button",
            "body":{"text":str(title)},
            "action": {
                "buttons":[
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_1",
                            "title": "Purple"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_2",
                            "title": "Balck"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "UNIQUE_BUTTON_ID_3",
                            "title": "Pink"
                        }
                    }
                ]
            }
       }
    }
    response = requests.post(WHATSAPP_URL, headers=header, json=data)
    ans = response.json()
    return ans
from messenger.account.models import WAMessageCampaign, WAMessageDeliverability

def select_message_by_id(wa_message_id):
    try:
        message = WAMessageCampaign.objects.get(wa_message_id=wa_message_id)
    except:
        print("ERROR [select_message_by_id]: There is no any messages for id: ", wa_message_id)
        return None
    return message


def is_deliverability(wa_message_id):
    try:
        message = WAMessageDeliverability.objects.get(wa_message_id=wa_message_id)
        print("WA_MESSAGE_ID: ",message)
        if message:
            return message
        else: 
            return None
    except:
        print('ERROR [is_deliverability]: There is no any messages for id: ', wa_message_id)
        return None
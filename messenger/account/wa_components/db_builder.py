from messenger.account.models import (
    WAMessageCampaign, 
    WAMessageDeliverability, 
    WAMessageError,
    WAMessageResponse,
)

from . import db_query

def build_wa_message_campaign(message, data):
    message_id = message
    try:
        campaign = WAMessageCampaign(
            message_id=message_id,
            messaging_product=data['messaging_product'],
            contact_input=data['contact_input'],
            contact_wa_id=data['contact_wa_id'],
            wa_message_id=data['wa_message_id'],
        )
        campaign.save()
    except:
        print('Error from build_wa_message_campaign')
        return False
    return True


def build_wa_message_deliverability(campaign, data):
    try:
        if 'status' in data and data['status'] == 'sent':
            deliverability = WAMessageDeliverability(
                campaign_id=campaign,
                messaging_product=data['messaging_product'],
                display_phone_number=data['display_phone_number'],
                phone_number_id=data['phone_number_id'],
                wa_message_id=data['wa_message_id'],
                is_sent=True,
                timestamp=data['timestamp'],
                recipient_id=data['recipient_id'],
                conversation_id=data['conversation_id'],
                expiration_timestamp=data['expiration_timestamp'],
            )
            deliverability.save()
        elif 'status' in data and data['status'] == 'delivered':
            message = db_query.is_deliverability(data['wa_message_id'])
            if message:
                message.is_delivered = True
                message.save()
            else:
                deliverability = WAMessageDeliverability(
                    campaign_id=campaign,
                    messaging_product=data['messaging_product'],
                    display_phone_number=data['display_phone_number'],
                    phone_number_id=data['phone_number_id'],
                    wa_message_id=data['wa_message_id'],
                    is_delivered=True,
                    timestamp=data['timestamp'],
                    recipient_id=data['recipient_id'],
                    conversation_id=data['conversation_id'],
                    expiration_timestamp=data['expiration_timestamp'],
                )
                deliverability.save()

        elif 'status' in data and data['status'] == 'read':
            message = db_query.is_deliverability(data['wa_message_id'])
            if message:
                message.is_read = True
                message.save()
            else:
                deliverability = WAMessageDeliverability(
                    campaign_id=campaign,
                    messaging_product=data['messaging_product'],
                    display_phone_number=data['display_phone_number'],
                    phone_number_id=data['phone_number_id'],
                    wa_message_id=data['wa_message_id'],
                    is_read=True,
                    timestamp=data['timestamp'],
                    recipient_id=data['recipient_id'],
                    conversation_id=data['conversation_id'],
                    expiration_timestamp=data['expiration_timestamp'],
                )
                deliverability.save()
        else:
            pass

    except:
        print('ERROR: Something goes wrong with data from build_wa_message_deliverability')
        return False
    return True


def build_wa_message_error(campaign, data):
    try:
        error = WAMessageError(
            campaign_id=campaign,
            messaging_product=data['messaging_product'],
            display_phone_number=data['display_phone_number'],
            phone_number_id=data['phone_number_id'],
            wa_message_id=data['wa_message_id'],
            timestamp=data['timestamp'],
            recipient_id=data['recipient_id'],
            error_code=data['error_code'],
            error_title=data['error_title'],
            error_message=data['error_message'],
            error_details=data['error_details'],
            error_href=data['error_href'],
        )
        error.save()
    except:
        print('ERROR: Something goes wrong with data from build_wa_message_error')
        return False
    return True


def build_wa_message_response(campaign, data):
    try:
        response = WAMessageResponse(
            wa_message_id = campaign,
            messaging_product=data['messaging_product'],
            display_phone_number=data['display_phone_number'],
            phone_number_id=data['phone_number_id'],
            response_from=data['from'],
            message_id=data['message_id'],
            timestamp=data['timestamp'],
            message_body=data['message_body'],
        )
        response.save()
    except:
        print('ERROR: Something goes wrong with data from build_wa_message_response')
        return False
    return True
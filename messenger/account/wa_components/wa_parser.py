

def get_webhook_parser(webhook):
    data = dict()
    try:
        data['messaging_product'] = webhook['messaging_product']
        data['contact_input'] = webhook['contacts'][0]['input']
        data['contact_wa_id'] = webhook['contacts'][0]['wa_id']
        data['wa_message_id'] = webhook['messages'][0]['id']
    except:
        print('Error from get_webhook_parser')
        return None
    return data



def post_webhook_parser(webhook):
    
    data = dict()
    try:
        # if message is successfully sent
        if 'statuses' in webhook['entry'][0]['changes'][0]['value'] and webhook['entry'][0]['changes'][0]['value']['statuses'][0]['status'] != 'failed':
            # print(50*"^")
            data['messaging_product'] = webhook['entry'][0]['changes'][0]['value']['messaging_product']
            data['display_phone_number'] = webhook['entry'][0]['changes'][0]['value']['metadata']['display_phone_number']
            data['phone_number_id'] = webhook['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
            data['wa_message_id'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['id']
            data['status'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['status']
            data['timestamp'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['timestamp']
            data['recipient_id'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['recipient_id']
            if 'conversation' in webhook['entry'][0]['changes'][0]['value']['statuses'][0] and 'id' in webhook['entry'][0]['changes'][0]['value']['statuses'][0]['conversation']:
                data['conversation_id'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['conversation']['id']
            if 'conversation' in webhook['entry'][0]['changes'][0]['value']['statuses'][0] and 'expiration_timestamp' in webhook['entry'][0]['changes'][0]['value']['statuses'][0]['conversation']:
                data['expiration_timestamp'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['conversation']['expiration_timestamp']

        # if message has a reply from contact
        elif 'from' in webhook['entry'][0]['changes'][0]['value']['messages'][0]:
            
            data['messaging_product'] = webhook['entry'][0]['changes'][0]['value']['messaging_product'] 
            data['display_phone_number'] = webhook['entry'][0]['changes'][0]['value']['metadata']['display_phone_number']    
            data['phone_number_id'] = webhook['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']    
            data['wa_message_id'] = webhook['entry'][0]['changes'][0]['value']['messages'][0]['context']['id']    
            data['from'] = webhook['entry'][0]['changes'][0]['value']['messages'][0]['from']           
            data['message_id'] = webhook['entry'][0]['changes'][0]['value']['messages'][0]['id']            
            data['timestamp'] = webhook['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']            
            data['message_body'] = webhook['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            
        # if message is failed
        else:
            data['messaging_product'] = webhook['entry'][0]['changes'][0]['value']['messaging_product']
            data['display_phone_number'] = webhook['entry'][0]['changes'][0]['value']['metadata']['display_phone_number']
            data['phone_number_id'] = webhook['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
            data['wa_message_id'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['id']
            data['status'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['status']
            data['timestamp'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['timestamp']
            data['recipient_id'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['recipient_id']
            data['error_code'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['errors'][0]['code']
            data['error_title'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['errors'][0]['title']
            data['error_message'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['errors'][0]['message']
            data['error_details'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['errors'][0]['error_data']['details']
            data['error_href'] = webhook['entry'][0]['changes'][0]['value']['statuses'][0]['errors'][0]['href']

    except:
        print('Error from post_webhook_parser')
        return None
    return data
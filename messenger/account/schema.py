import graphene
from graphene_django import DjangoObjectType, DjangoListField
from . import models



class WAMessagesType(DjangoObjectType):
    class Meta:
        model = models.WAMessage
        fields = (
            'id',
            'title',
            'slug',
            'message_body',
            'status',
            'created_on',
            'updated_on',
        )


class WAMessageCampaignType(DjangoObjectType):
    class Meta:
        model = models.WAMessageCampaign
        fields = (
            'id',
            'message_id',
            'messaging_product',
            'contact_input',
            'contact_wa_id',
            'wa_message_id',
            'created_on',
        )


class WAMessageDeliverabilityType(DjangoObjectType):
    class Meta:
        model = models.WAMessageDeliverability
        fields = (
            'id',
            'campaign_id',
            'messaging_product',
            'display_phone_number',
            'phone_number_id',
            'wa_message_id',
            'is_sent',
            'is_delivered',
            'is_read',
            'timestamp',
            'recipient_id',
            'conversation_id',
            'expiration_timestamp',
            'created_on',
            'updated_on',
        )


class WAMessageResponseType(DjangoObjectType):
    class Meta:
        model = models.WAMessageResponse
        fields = (
            'id',
            'wa_message_id',
            'messaging_product',
            'display_phone_number',
            'phone_number_id',
            'response_from',
            'message_id',
            'timestamp',
            'message_body',
            'created_on',
            'updated_on',
        )


class WAMessageErrorType(DjangoObjectType):
    class Meta:
        model = models.WAMessage
        fields = (
            'id',
            'campaign_id',
            'messaging_product',
            'display_phone_number',
            'phone_number_id',
            'wa_message_id',
            'status',
            'timestamp',
            'recipient_id',
            'error_code',
            'error_title',
            'error_message',
            'error_details',
            'error_href',
            'created_on',
        )


class Query(graphene.ObjectType):
    #WA_Message_Queries:
#                                       WAMessages
    # Get all WA Messages
    all_wa_messages = DjangoListField(WAMessagesType)

    # Get WA Message by Id
    get_wa_message_by_id = graphene.Field(WAMessagesType, id=graphene.Int())
    def resolve_get_wa_message_by_id(root, info, id):
        return models.WAMessage.objects.get(pk=id)
    
#                                       Campaigns    
    # Get all WA Campaigns
    all_wa_campaigns = DjangoListField(WAMessageCampaignType)

#                                      Deliverability
    # Get all data from Deliverabilities
    all_wa_message_deliverability = DjangoListField(WAMessageDeliverabilityType)

#                                        Response

    all_wa_message_response = DjangoListField(WAMessageResponseType)

#                                         Errors
    all_wa_message_error = DjangoListField(WAMessageErrorType)


    
schema = graphene.Schema(query=Query)
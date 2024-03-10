from django.contrib import admin
from . import models

@admin.register(models.WAMessage)
class WAMessageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
        'created_on',
        'updated_on',
    ]
    list_filter = [
        'created_on',
        'updated_on',
    ]
    search_fields = [
        'title',
        'message_body',
    ]
    prepopulated_fields = {'slug':['title']}
    date_hierarchy = 'created_on'
    ordering = ['created_on', 'updated_on']


@admin.register(models.WAMessageCampaign)
class WAMessageCampaignAdmin(admin.ModelAdmin):
    list_display = [
        'message_id',
        'messaging_product',
        'contact_input',
        'contact_wa_id',
        'wa_message_id',
        'created_on',
    ]
    ordering = ['created_on']


@admin.register(models.WAMessageDeliverability)
class WAMessageDeliverabilityAdmin(admin.ModelAdmin):
    list_display = [
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
    ]
    ordering = ['created_on']


@admin.register(models.WAMessageError)
class WAMessageErrorAdmin(admin.ModelAdmin):
    list_display = [
        'campaign_id',
        'messaging_product',
        'display_phone_number',
        'phone_number_id',
        'wa_message_id',
        'timestamp',
        'recipient_id',
        'error_code',
        'error_title',
        'error_message',
        'error_details',
        'error_href',
        'created_on',
    ]
    ordering = ['created_on']


@admin.register(models.WAMessageResponse)
class WAMessageErrorResponse(admin.ModelAdmin):
    list_display = [
        'wa_message_id',
        'messaging_product',
        'display_phone_number',
        'phone_number_id',
        'response_from',
        'message_id',
        'timestamp',
        'message_body',
        'created_on',
    ]
    ordering = ['created_on']
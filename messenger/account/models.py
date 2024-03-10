from django.db import models
from django.utils.translation import gettext_lazy as _

#                                BD WA Messages

class WAMessage(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        ACTIVE = 'AC', 'Active'

    title = models.CharField(
        max_length=50, 
        null=False, 
        unique=True, 
        blank=False, 
        verbose_name=_("Message Title"),
        help_text=_("format: required, max-50"),
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Message safe URL"),
        help_text=_("format: required, letters, numbers, underscore or hyphens"),
    )
    message_body = models.TextField(
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_("Message Body"),
        help_text=_("format: required"),
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date Message created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date Message last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ["created_on"]

    def __str__(self):
        return self.title


class WAMessageCampaign(models.Model):
    message_id = models.ForeignKey(
        WAMessage,
        on_delete=models.PROTECT,
    )
    messaging_product = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("messaging_product"),
        help_text=_("format: not required, max-50"),
    )
    contact_input = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("contact_input"),
        help_text=_("format: not required, max-50"),
    )
    contact_wa_id = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("contact_wa_id"),
        help_text=_("format: not required, max-50"),
    )
    wa_message_id = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("sent_message_id"),
        help_text=_("format: not required, max-250"),
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date Activity created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")
        ordering = ["created_on"]


class WAMessageDeliverability(models.Model):
    campaign_id = models.ForeignKey(
        WAMessageCampaign,
        on_delete=models.PROTECT,
    )
    messaging_product = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("messageing_product"),
        help_text=_("format: not required, max-50"),
    )
    display_phone_number = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("display_phone_number"),
        help_text=_("format: not required, max-50"),
    )
    phone_number_id = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("phone_number_id"),
        help_text=_("format: not required, max-50"),
    )
    wa_message_id = models.CharField(
        max_length=250, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("wa_message_id"),
        help_text=_("format: not required, max-250"),
    )
    is_sent = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    timestamp = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("timestamp"),
        help_text=_("format: not required, max-50"),
    )
    recipient_id = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("contact_input"),
        help_text=_("format: not required, max-50"),
    )
    conversation_id = models.CharField(
        max_length=200, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("conversation_id"),
        help_text=_("format: not required, max-200"),
    )
    expiration_timestamp = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("expiration_timestamp"),
        help_text=_("format: not required, max-50"),
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date Row created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date Row last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Deliverability")
        verbose_name_plural = _("Deliverabilities")
        ordering = ["created_on"]


class WAMessageResponse(models.Model):
    wa_message_id = models.ForeignKey(
        WAMessageCampaign,
        on_delete=models.CASCADE,
    )
    messaging_product = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("messageing_product"),
        help_text=_("format: not required, max-50"),
    )
    display_phone_number = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("display_phone_number"),
        help_text=_("format: not required, max-50"),
    )
    phone_number_id = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("phone_number_id"),
        help_text=_("format: not required, max-50"),
    )
    response_from = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("response_from"),
        help_text=_("format: not required, max-50"),
    )
    message_id = models.CharField(
        max_length=150, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("message_id"),
        help_text=_("format: not required, max-150"),
    )
    timestamp = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("timestamp"),
        help_text=_("format: not required, max-50"),
    )
    message_body = models.TextField(
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_("Message Body"),
        help_text=_("format: required"),
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date Row created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date Row last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")
        ordering = ["created_on"]


class WAMessageError(models.Model):
    campaign_id = models.ForeignKey(
        WAMessageCampaign,
        on_delete=models.PROTECT,
    )
    messaging_product = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("messageing_product"),
        help_text=_("format: not required, max-50"),
    )
    display_phone_number = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("display_phone_number"),
        help_text=_("format: not required, max-50"),
    )
    phone_number_id = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("phone_number_id"),
        help_text=_("format: not required, max-50"),
    )
    wa_message_id = models.CharField(
        max_length=250, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("wa_message_id"),
        help_text=_("format: not required, max-250"),
    )
    status = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("status"),
        help_text=_("format: not required, max-50"),
    )
    timestamp = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("timestamp"),
        help_text=_("format: not required, max-50"),
    )
    recipient_id = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("recipient_id"),
        help_text=_("format: not required, max-50"),
    )
    error_code = models.CharField(
        max_length=200, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("error_code"),
        help_text=_("format: not required, max-200"),
    )
    error_title = models.CharField(
        max_length=50, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("error_title"),
        help_text=_("format: not required, max-50"),
    )
    error_message = models.CharField(
        max_length=150, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("error_message"),
        help_text=_("format: not required, max-150"),
    )
    error_details = models.TextField( 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("error_details"),
        help_text=_("format: not required"),
    )
    error_href = models.CharField(
        max_length=250, 
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_("error_href"),
        help_text=_("format: not required, max-250"),
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("Date Row created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("Error")
        verbose_name_plural = _("Errors")
        ordering = ["created_on"]
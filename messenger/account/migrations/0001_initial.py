# Generated by Django 4.2.5 on 2024-01-06 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WAMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='format: required, max-50', max_length=50, unique=True, verbose_name='Message Title')),
                ('slug', models.SlugField(help_text='format: required, letters, numbers, underscore or hyphens', max_length=255, verbose_name='Message safe URL')),
                ('message_body', models.TextField(help_text='format: required', verbose_name='Message Body')),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('AC', 'Active')], default='DF', max_length=2)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Message created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Message last updated')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='WAMessageCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messaging_product', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='messaging_product')),
                ('contact_input', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='contact_input')),
                ('contact_wa_id', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='contact_wa_id')),
                ('wa_message_id', models.CharField(blank=True, help_text='format: not required, max-250', max_length=50, null=True, verbose_name='sent_message_id')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Activity created')),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.wamessage')),
            ],
            options={
                'verbose_name': 'Campaign',
                'verbose_name_plural': 'Campaigns',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='WAMessageResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messaging_product', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='messageing_product')),
                ('display_phone_number', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='display_phone_number')),
                ('phone_number_id', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='phone_number_id')),
                ('response_from', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='response_from')),
                ('message_id', models.CharField(blank=True, help_text='format: not required, max-150', max_length=150, null=True, verbose_name='message_id')),
                ('timestamp', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='timestamp')),
                ('message_body', models.TextField(help_text='format: required', verbose_name='Message Body')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Row created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Row last updated')),
                ('wa_message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.wamessagecampaign')),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='WAMessageError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messaging_product', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='messageing_product')),
                ('display_phone_number', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='display_phone_number')),
                ('phone_number_id', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='phone_number_id')),
                ('wa_message_id', models.CharField(blank=True, help_text='format: not required, max-250', max_length=250, null=True, verbose_name='wa_message_id')),
                ('status', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='status')),
                ('timestamp', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='timestamp')),
                ('recipient_id', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='recipient_id')),
                ('error_code', models.CharField(blank=True, help_text='format: not required, max-200', max_length=200, null=True, verbose_name='error_code')),
                ('error_title', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='error_title')),
                ('error_message', models.CharField(blank=True, help_text='format: not required, max-150', max_length=150, null=True, verbose_name='error_message')),
                ('error_details', models.TextField(blank=True, help_text='format: not required', null=True, verbose_name='error_details')),
                ('error_href', models.CharField(blank=True, help_text='format: not required, max-250', max_length=250, null=True, verbose_name='error_href')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Row created')),
                ('campaign_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.wamessagecampaign')),
            ],
            options={
                'verbose_name': 'Error',
                'verbose_name_plural': 'Errors',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='WAMessageDeliverability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messaging_product', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='messageing_product')),
                ('display_phone_number', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='display_phone_number')),
                ('phone_number_id', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='phone_number_id')),
                ('wa_message_id', models.CharField(blank=True, help_text='format: not required, max-250', max_length=250, null=True, verbose_name='wa_message_id')),
                ('is_sent', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='timestamp')),
                ('recipient_id', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='contact_input')),
                ('conversation_id', models.CharField(blank=True, help_text='format: not required, max-200', max_length=200, null=True, verbose_name='conversation_id')),
                ('expiration_timestamp', models.CharField(blank=True, help_text='format: not required, max-50', max_length=50, null=True, verbose_name='expiration_timestamp')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Row created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='Date Row last updated')),
                ('campaign_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.wamessagecampaign')),
            ],
            options={
                'verbose_name': 'Deliverability',
                'verbose_name_plural': 'Deliverabilities',
                'ordering': ['created_on'],
            },
        ),
    ]

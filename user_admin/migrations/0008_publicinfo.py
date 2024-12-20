# Generated by Django 5.1.1 on 2024-11-23 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0007_eventnotification_remove_event_attachment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='public_info', to='user_admin.userinfo')),
            ],
        ),
    ]

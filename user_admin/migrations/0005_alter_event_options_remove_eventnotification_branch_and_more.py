# Generated by Django 5.1.2 on 2024-11-20 21:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0004_auto_20241121_0516'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='eventnotification',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='eventnotification',
            name='user_type',
        ),
        migrations.AddField(
            model_name='eventnotification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]

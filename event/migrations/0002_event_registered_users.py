# Generated by Django 5.0.6 on 2024-05-28 14:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registered_users',
            field=models.ManyToManyField(related_name='registered_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
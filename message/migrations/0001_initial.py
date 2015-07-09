# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver_deleted', models.BooleanField(default=False)),
                ('sender_deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('receiver_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='received_message')),
                ('sender_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sended_message')),
            ],
        ),
    ]

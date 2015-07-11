# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20150703_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite_post', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='liked_post', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]

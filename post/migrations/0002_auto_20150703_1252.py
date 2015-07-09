# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='favorite',
            field=models.ManyToManyField(null=True, related_name='favorite_post', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(null=True, related_name='liked_post', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='root_post',
            field=models.ForeignKey(blank=True, null=True, to='post.Post'),
        ),
    ]

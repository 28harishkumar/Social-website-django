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
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('attachment_type', models.CharField(choices=[('img', 'Image'), ('video', 'Video'), ('pdf', 'PDF File'), ('audio', 'Audio File'), ('txt', 'Text File'), ('url', 'Link')], blank=True, max_length=10, null=True)),
                ('attachment', models.CharField(blank=True, max_length=250, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('favorite', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='favorite_post')),
                ('like', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='liked_post')),
                ('root_post', models.ForeignKey(to='post.Post')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

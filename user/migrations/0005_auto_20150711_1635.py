# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20150711_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_image',
            field=sorl.thumbnail.fields.ImageField(upload_to='user/cover', default='default_cover.jpg'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=sorl.thumbnail.fields.ImageField(upload_to='user/profile', default='default_profile.jpg'),
        ),
    ]

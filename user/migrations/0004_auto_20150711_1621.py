# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150703_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cover_image',
            field=models.ImageField(default='default_cover.jpg', upload_to='user/cover'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='default_profile.jpg', upload_to='user/profile'),
        ),
    ]

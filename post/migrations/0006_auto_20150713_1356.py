# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20150713_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='attachment_type',
            field=models.CharField(choices=[('img', 'Image'), ('video', 'Video'), ('file', 'File'), ('audio', 'Audio')], blank=True, null=True, max_length=10),
        ),
    ]

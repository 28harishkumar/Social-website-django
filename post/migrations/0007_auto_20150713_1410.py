# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20150713_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='attachment_type',
            field=models.CharField(null=True, choices=[('image', 'Image'), ('video', 'Video'), ('file', 'File'), ('audio', 'Audio')], max_length=10, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='on_comment',
            field=models.ForeignKey(blank=True, null=True, related_name='reply', to='comment.Comment'),
        ),
    ]

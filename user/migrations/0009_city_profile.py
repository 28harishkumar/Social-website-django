# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20150711_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('IND', 'India')], max_length=3)),
                ('region', models.CharField(choices=[('AS', 'Asia'), ('Af', 'Africa'), ('EU', 'Europe'), ('NA', 'North Amarica'), ('SA', 'South Amarica')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('work_at', models.CharField(null=True, blank=True, max_length=100)),
                ('website', models.URLField(null=True, blank=True)),
                ('data_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(null=True, choices=[('m', 'MALE'), ('f', 'FEMALE'), ('n', 'NONE')], max_length=1, blank=True)),
                ('language', models.CharField(null=True, choices=[('ENG', 'English'), ('HIN', 'Hindi')], max_length=5, blank=True)),
                ('Quote', models.CharField(null=True, blank=True, max_length=200)),
                ('live_in', models.ForeignKey(null=True, to='user.City', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

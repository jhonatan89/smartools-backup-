# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clientfirtsName', models.CharField(max_length=200)),
                ('clientLastName', models.CharField(max_length=200)),
                ('clientEmail', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
                ('uploadDate', models.DateTimeField(auto_now_add=True)),
                ('originalVideoPath', models.CharField(max_length=255)),
                ('convertedVideoPath', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2, choices=[(b'CON', b'Converted'), (b'WFC', b'Waiting for conversion')])),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AlterField(
            model_name='video',
            name='originalVideoPath',
            field=models.FileField(upload_to=b'video/%Y/%m/%d', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0004_auto_20150916_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='originalVideoPath',
            field=models.FileField(upload_to=b'video/%Y/%m/%d'),
        ),
    ]

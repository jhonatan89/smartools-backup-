# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0003_auto_20150912_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.CharField(default=b'WFC', max_length=3, choices=[(b'CON', b'Converted'), (b'WFC', b'Waiting for conversion')]),
        ),
    ]

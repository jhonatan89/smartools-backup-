# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Competition', '0002_competition_company'),
        ('Video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='competition',
            field=models.ForeignKey(blank=True, to='Competition.Competition', null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to=b'video/%Y/%m/%d', blank=True),
        ),
    ]

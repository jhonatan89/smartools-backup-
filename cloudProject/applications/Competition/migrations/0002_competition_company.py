# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
        ('Competition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='company',
            field=models.ForeignKey(to='Company.Company', null=True),
        ),
    ]

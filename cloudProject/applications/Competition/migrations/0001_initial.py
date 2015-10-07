# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'ImageCompetitions/%Y/%m/%d')),
                ('startDate', models.DateTimeField(auto_now_add=True)),
                ('endDate', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
                ('company', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150725_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='set',
            field=models.ForeignKey(verbose_name='Related Files', to='events.SetOfFiles'),
        ),
        migrations.AlterField(
            model_name='setoffiles',
            name='name',
            field=models.CharField(max_length=225),
        ),
    ]

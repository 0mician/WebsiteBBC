# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20150730_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(help_text='Give a short description of the event, it will be displayed on the homepage under events (max 500 characters)', max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text="Give a meaningful name to the event, for example 'Belgian Brain Congress 2015' (max 255 characters)", max_length=255),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(help_text='Give a meaningful name to the file, this name will be displayed on the webpage (max 255 characters)', max_length=255, default='meaningful filename'),
            preserve_default=False,
        ),
    ]

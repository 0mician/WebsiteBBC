# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20150731_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=tinymce.models.HTMLField(help_text='This is for the event page, you can use style here, and are free to add as much content as you like', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, help_text='optional, could be a link to the website of the event', null=True),
        ),
        migrations.AlterField(
            model_name='setoffiles',
            name='name',
            field=models.CharField(help_text="Give a meaningful name to the set of file, for example 'BBCongress2015' (max 225 characters)", max_length=225),
        ),
    ]

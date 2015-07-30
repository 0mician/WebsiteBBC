# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setoffiles',
            options={'verbose_name_plural': 'Set of files'},
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='This should be a short description of the event for the frontpage', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='uploaded_files',
            field=models.ForeignKey(blank=True, null=True, to='events.SetOfFiles'),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

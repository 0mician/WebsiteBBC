# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150729_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='details',
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(),
        ),
    ]

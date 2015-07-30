# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20150729_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=3, default='OTH', choices=[('BAW', 'Brain Awareness Week'), ('BBC', 'Belgian Brain Congress'), ('EBC', 'European Brain Council'), ('OTH', 'Other')]),
            preserve_default=False,
        ),
    ]

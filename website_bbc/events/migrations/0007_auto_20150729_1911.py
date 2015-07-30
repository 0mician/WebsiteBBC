# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_details_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20150729_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='details_test',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
    ]

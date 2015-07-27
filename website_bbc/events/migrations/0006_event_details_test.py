# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20150727_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='details_test',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]

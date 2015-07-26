# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150725_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='uploaded_files',
            field=models.ForeignKey(to='events.SetOfFiles', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='set',
        ),
        migrations.AddField(
            model_name='event',
            name='uploaded_files',
            field=models.FileField(upload_to='', null=True),
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='SetOfFiles',
        ),
    ]

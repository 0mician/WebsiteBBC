# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20150717_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_contact',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='name_contact',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='society',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='title_contact',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20150716_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='society',
        ),
        migrations.AddField(
            model_name='member',
            name='address_contact',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email_contact',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='fax_contact',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='gsm_contact',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='name_contact',
            field=models.TextField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_contact',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='registration_number',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='title_contact',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='website_contact',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]

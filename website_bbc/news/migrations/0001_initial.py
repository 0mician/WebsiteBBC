# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20150905_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(help_text='Give a meaningful name to the news (max 255 characters)', max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('url', models.URLField(blank=True, help_text='optional, could be a link to a website, more URL can be added in the details section', null=True)),
                ('date', models.DateField()),
                ('description', models.CharField(help_text='Give a short description of the event, it will be displayed on the homepage under events (max 500 characters)', max_length=500)),
                ('details', tinymce.models.HTMLField(help_text='This is for the news details page, you can use style here, and are free to add as much content as you like', null=True)),
                ('uploaded_files', models.ForeignKey(blank=True, to='events.SetOfFiles', null=True)),
            ],
        ),
    ]

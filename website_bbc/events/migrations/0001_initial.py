# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('location', models.CharField(null=True, max_length=255, blank=True)),
                ('details', models.TextField(max_length=10000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='', storage=django.core.files.storage.FileSystemStorage(location='../files/'))),
            ],
        ),
        migrations.CreateModel(
            name='SetOfFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='set name')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='set',
            field=models.ForeignKey(to='events.SetOfFiles', verbose_name='set'),
        ),
    ]

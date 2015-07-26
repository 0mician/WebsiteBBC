# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150723_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SetOfFiles',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='set name', max_length=225)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='uploaded_files',
            field=models.ForeignKey(null=True, to='events.File'),
        ),
        migrations.AddField(
            model_name='file',
            name='set',
            field=models.ForeignKey(to='events.SetOfFiles', verbose_name='set'),
        ),
    ]

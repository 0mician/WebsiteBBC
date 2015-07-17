# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('title', models.TextField(blank=True, max_length=400)),
                ('address', models.TextField(blank=True, max_length=400)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('gsm', models.CharField(blank=True, max_length=20)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('society', models.ForeignKey(to='members.Member')),
            ],
        ),
        migrations.RemoveField(
            model_name='representative',
            name='society',
        ),
        migrations.DeleteModel(
            name='Representative',
        ),
    ]

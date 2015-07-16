# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('society', models.CharField(max_length=250, unique=True)),
                ('category', models.CharField(max_length=2, choices=[('PH', 'Pharmaceutical Company'), ('PA', 'Patient Association'), ('SC', 'Scientific Society')])),
                ('address', models.TextField(max_length=400)),
                ('phone', models.CharField(max_length=20)),
                ('gsm', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField(max_length=200)),
                ('title', models.TextField(max_length=400)),
                ('address', models.TextField(max_length=400)),
                ('phone', models.CharField(max_length=20)),
                ('gsm', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('society', models.ForeignKey(to='Members.Member')),
            ],
        ),
    ]

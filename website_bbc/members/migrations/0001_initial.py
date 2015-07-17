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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('society', models.CharField(max_length=250, unique=True)),
                ('address', models.TextField(max_length=400, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('gsm', models.CharField(max_length=20, blank=True)),
                ('fax', models.CharField(max_length=20, blank=True)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=200)),
                ('title', models.TextField(max_length=400, blank=True)),
                ('address', models.TextField(max_length=400, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('gsm', models.CharField(max_length=20, blank=True)),
                ('fax', models.CharField(max_length=20, blank=True)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientAssocMember',
            fields=[
                ('member_ptr', models.OneToOneField(serialize=False, parent_link=True, to='members.Member', auto_created=True, primary_key=True)),
            ],
            bases=('members.member',),
        ),
        migrations.CreateModel(
            name='PharmaMember',
            fields=[
                ('member_ptr', models.OneToOneField(serialize=False, parent_link=True, to='members.Member', auto_created=True, primary_key=True)),
            ],
            bases=('members.member',),
        ),
        migrations.CreateModel(
            name='ScientificSocietyMember',
            fields=[
                ('member_ptr', models.OneToOneField(serialize=False, parent_link=True, to='members.Member', auto_created=True, primary_key=True)),
            ],
            bases=('members.member',),
        ),
        migrations.AddField(
            model_name='representative',
            name='society',
            field=models.ForeignKey(to='members.Member'),
        ),
    ]

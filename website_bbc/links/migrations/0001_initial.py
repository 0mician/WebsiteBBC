# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the association', max_length=255)),
                ('url', models.URLField(help_text="link to the association's website")),
            ],
            options={
                'verbose_name_plural': 'Links',
            },
        ),
    ]

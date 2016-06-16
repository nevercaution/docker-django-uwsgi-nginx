# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=255)),
                ('create_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'contents',
                'managed': True,
            },
        ),
    ]

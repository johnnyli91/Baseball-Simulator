# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='team',
            field=models.ManyToManyField(to='Baseball.Team'),
        ),
    ]

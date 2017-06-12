# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0009_player_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='AB',
            field=models.IntegerField(default=0),
        ),
    ]

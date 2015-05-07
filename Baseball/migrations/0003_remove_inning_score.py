# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0002_game_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inning',
            name='score',
        ),
    ]

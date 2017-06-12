# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0010_player_ab'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='runs',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pitcher_contact',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_control',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_double',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_flyout',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_groundout',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_homerun',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_movement',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_power',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_single',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_strikeout',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_triple',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='player',
            name='pitcher_walk',
            field=models.IntegerField(default=1),
        ),
    ]

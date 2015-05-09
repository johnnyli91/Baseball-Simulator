# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0004_inning_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
                ('game', models.ForeignKey(related_name='game_score', to='Baseball.Game')),
                ('team', models.ForeignKey(related_name='team_score', to='Baseball.Team')),
            ],
        ),
    ]

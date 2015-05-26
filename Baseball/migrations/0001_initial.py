# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.IntegerField(choices=[(1, b'Single'), (2, b'Double'), (3, b'Triple'), (4, b'Home Run'), (5, b'Walk'), (6, b'Strikeout'), (7, b'Groundout'), (8, b'Flyout')])),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Inning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('score', models.IntegerField(null=True)),
                ('game', models.ForeignKey(related_name='inning', to='Baseball.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('power', models.IntegerField()),
                ('eye', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('batter_contact', models.IntegerField()),
                ('batter_single', models.IntegerField()),
                ('batter_double', models.IntegerField()),
                ('batter_triple', models.IntegerField()),
                ('batter_homerun', models.IntegerField()),
                ('batter_walk', models.IntegerField()),
                ('batter_strikeout', models.IntegerField()),
                ('batter_groundout', models.IntegerField()),
                ('batter_flyout', models.IntegerField()),
                ('batter_speed', models.IntegerField()),
                ('pitcher_contact', models.IntegerField(default=0)),
                ('pitcher_single', models.IntegerField(default=0)),
                ('pitcher_double', models.IntegerField(default=0)),
                ('pitcher_triple', models.IntegerField(default=0)),
                ('pitcher_homerun', models.IntegerField(default=0)),
                ('pitcher_walk', models.IntegerField(default=0)),
                ('pitcher_strikeout', models.IntegerField(default=0)),
                ('pitcher_groundout', models.IntegerField(default=0)),
                ('pitcher_flyout', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
                ('game', models.ForeignKey(related_name='game_score', to='Baseball.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='team',
            field=models.ForeignKey(related_name='team_score', to='Baseball.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name='team_player', to='Baseball.Team'),
        ),
        migrations.AddField(
            model_name='inning',
            name='team',
            field=models.ForeignKey(related_name='inning', to='Baseball.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team',
            field=models.ManyToManyField(to='Baseball.Team'),
        ),
        migrations.AddField(
            model_name='bat',
            name='inning',
            field=models.ForeignKey(related_name='inning', to='Baseball.Inning'),
        ),
        migrations.AddField(
            model_name='bat',
            name='player',
            field=models.ForeignKey(related_name='bat', to='Baseball.Player'),
        ),
    ]

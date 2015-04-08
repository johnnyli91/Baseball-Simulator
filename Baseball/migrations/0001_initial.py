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
                ('result', models.IntegerField(choices=[(0, b'Out'), (1, b'Single'), (2, b'Double'), (3, b'Triple'), (4, b'Home Run')])),
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
                ('score', models.IntegerField()),
                ('game', models.ForeignKey(related_name='inning', to='Baseball.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('power', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('pitch', models.IntegerField()),
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

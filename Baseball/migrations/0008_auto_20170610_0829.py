# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0007_team_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='AVG',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='BB',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='CS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='HR',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='K',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='OBP',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='RBI',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='SB',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='SLG',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='doubles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='games',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='triples',
            field=models.IntegerField(default=0),
        ),
    ]

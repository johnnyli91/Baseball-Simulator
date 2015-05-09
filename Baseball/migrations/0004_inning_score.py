# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0003_remove_inning_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='inning',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]

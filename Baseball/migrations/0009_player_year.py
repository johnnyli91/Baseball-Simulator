# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0008_auto_20170610_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]

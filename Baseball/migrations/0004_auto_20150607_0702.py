# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0003_auto_20150607_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bat',
            name='inning',
            field=models.ForeignKey(related_name='bat_inning', to='Baseball.Inning'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Baseball', '0002_auto_20150531_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bat',
            name='inning',
            field=models.ForeignKey(related_name='bat', to='Baseball.Inning'),
        ),
    ]

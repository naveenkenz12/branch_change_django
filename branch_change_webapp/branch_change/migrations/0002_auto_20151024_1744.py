# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='cpi',
            field=models.DecimalField(verbose_name='CPI', decimal_places=2, max_digits=5),
            preserve_default=True,
        ),
    ]

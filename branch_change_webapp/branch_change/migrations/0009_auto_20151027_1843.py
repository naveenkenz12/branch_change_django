# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0008_branch_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_stats',
            name='cutoff',
            field=models.DecimalField(verbose_name='Cutoff', decimal_places=5, max_digits=10),
        ),
    ]

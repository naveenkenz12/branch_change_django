# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0009_auto_20151027_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_stats',
            name='cutoff',
            field=models.CharField(max_length=10, verbose_name='Cutoff'),
        ),
        migrations.AlterField(
            model_name='branch_stats',
            name='final_st',
            field=models.CharField(max_length=10, verbose_name='Final Strength'),
        ),
        migrations.AlterField(
            model_name='branch_stats',
            name='original_st',
            field=models.CharField(max_length=10, verbose_name='Original Strength'),
        ),
        migrations.AlterField(
            model_name='branch_stats',
            name='sanctioned_st',
            field=models.CharField(max_length=10, verbose_name='Sanctioned Strength'),
        ),
    ]

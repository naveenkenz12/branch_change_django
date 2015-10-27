# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0007_allocated_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch_stats',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('branch_name', models.CharField(verbose_name='Branch Name', max_length=25)),
                ('cutoff', models.DecimalField(decimal_places=2, verbose_name='Cutoff', max_digits=5)),
                ('sanctioned_st', models.IntegerField(verbose_name='Sanctioned Strength')),
                ('original_st', models.IntegerField(verbose_name='Original Strength')),
                ('final_st', models.IntegerField(verbose_name='Final Strength')),
            ],
        ),
    ]

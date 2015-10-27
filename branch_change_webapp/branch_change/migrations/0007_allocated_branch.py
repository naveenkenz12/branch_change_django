# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0006_auto_20151027_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='allocated_branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('roll_number', models.CharField(max_length=9, verbose_name='roll number')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('initial_branch', models.CharField(max_length=25, verbose_name='initial branch')),
                ('alloted_branch', models.CharField(max_length=25, verbose_name='alloted branch')),
            ],
        ),
    ]

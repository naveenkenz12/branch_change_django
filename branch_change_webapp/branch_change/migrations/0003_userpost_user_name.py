# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0002_auto_20151024_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='user_name',
            field=models.CharField(verbose_name='username', max_length=100, default=''),
            preserve_default=False,
        ),
    ]

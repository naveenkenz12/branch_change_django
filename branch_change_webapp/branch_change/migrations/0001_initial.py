# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userpost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('roll_number', models.CharField(max_length=9, verbose_name='Roll No')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('present_branch', models.CharField(max_length=25, choices=[('aebtech', 'AE B.Tech'), ('cebtech', 'CE B.Tech'), ('ch', 'CH'), ('clbtech', 'CL B.Tech'), ('cldualdeg', 'CL Dual Deg'), ('csbtech', 'CS B.Tech'), ('eebtech', 'EE B.Tech'), ('eedualdege1', 'EE Dual Deg E1'), ('eedualdege2', 'EE Dual Deg E2'), ('endualdeg', 'EN Dual Deg'), ('epbtech', 'EP B.Tech'), ('epdualdegn1', 'EP Dual Deg N1'), ('mebtech', 'ME B.Tech'), ('medualdegm2', 'ME Dual Deg M2'), ('mmbtech', 'MM B.Tech'), ('mmdualdegy1', 'MM Dual Deg Y1'), ('mmdualdegy2', 'MM Dual Deg Y2')], verbose_name='Present Branch')),
                ('category', models.CharField(max_length=5, default='GE', verbose_name='Category', choices=[('ge', 'GE'), ('obc', 'OBC'), ('sc', 'SC'), ('st', 'ST')])),
                ('cpi', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='CPI')),
                ('pref1', models.CharField(max_length=25, choices=[('aebtech', 'AE B.Tech'), ('cebtech', 'CE B.Tech'), ('ch', 'CH'), ('clbtech', 'CL B.Tech'), ('cldualdeg', 'CL Dual Deg'), ('csbtech', 'CS B.Tech'), ('eebtech', 'EE B.Tech'), ('eedualdege1', 'EE Dual Deg E1'), ('eedualdege2', 'EE Dual Deg E2'), ('endualdeg', 'EN Dual Deg'), ('epbtech', 'EP B.Tech'), ('epdualdegn1', 'EP Dual Deg N1'), ('mebtech', 'ME B.Tech'), ('medualdegm2', 'ME Dual Deg M2'), ('mmbtech', 'MM B.Tech'), ('mmdualdegy1', 'MM Dual Deg Y1'), ('mmdualdegy2', 'MM Dual Deg Y2')], verbose_name='Wish to go to Pref 1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

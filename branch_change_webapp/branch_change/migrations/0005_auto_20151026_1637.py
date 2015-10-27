# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch_change', '0004_auto_20151025_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='pref16',
        ),
        migrations.AlterField(
            model_name='userpost',
            name='category',
            field=models.CharField(verbose_name='Category', max_length=5, choices=[('GE', 'GE'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], default='GE'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref1',
            field=models.CharField(verbose_name='Wish to go to Pref 1', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref10',
            field=models.CharField(verbose_name='Wish to go to Pref 10', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref11',
            field=models.CharField(verbose_name='Wish to go to Pref 11', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref12',
            field=models.CharField(verbose_name='Wish to go to Pref 12', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref13',
            field=models.CharField(verbose_name='Wish to go to Pref 13', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref14',
            field=models.CharField(verbose_name='Wish to go to Pref 14', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref15',
            field=models.CharField(verbose_name='Wish to go to Pref 15', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref2',
            field=models.CharField(verbose_name='Wish to go to Pref 2', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref3',
            field=models.CharField(verbose_name='Wish to go to Pref 3', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref4',
            field=models.CharField(verbose_name='Wish to go to Pref 4', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref5',
            field=models.CharField(verbose_name='Wish to go to Pref 5', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref6',
            field=models.CharField(verbose_name='Wish to go to Pref 6', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref7',
            field=models.CharField(verbose_name='Wish to go to Pref 7', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref8',
            field=models.CharField(verbose_name='Wish to go to Pref 8', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pref9',
            field=models.CharField(verbose_name='Wish to go to Pref 9', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='present_branch',
            field=models.CharField(verbose_name='Present Branch', max_length=25, choices=[('', 'none'), ('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
    ]

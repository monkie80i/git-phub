# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20181027_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='extraversion',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='feeling',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='introversion',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='intuition',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='judging',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='percieving',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='sensing',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='thinking',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
    ]

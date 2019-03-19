# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0004_auto_20181027_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('user_data', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

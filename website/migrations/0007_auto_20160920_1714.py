# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-20 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20160920_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

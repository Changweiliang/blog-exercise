# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170919_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='post_tags',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

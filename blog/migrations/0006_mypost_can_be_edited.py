# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mypost_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='can_be_edited',
            field=models.BooleanField(default=False),
        ),
    ]
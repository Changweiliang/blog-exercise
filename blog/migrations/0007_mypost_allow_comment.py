# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_mypost_can_be_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypost',
            name='allow_comment',
            field=models.BooleanField(default=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 03:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_mypost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

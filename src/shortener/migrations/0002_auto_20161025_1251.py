# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gittaurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gittaurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable_blog', '0003_auto_20170227_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-27 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20170827_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='wished_by',
            field=models.ManyToManyField(related_name='wishing', to='login.User'),
        ),
    ]

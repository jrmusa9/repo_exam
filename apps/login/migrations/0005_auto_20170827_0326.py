# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-27 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_item_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wish',
        ),
        migrations.RemoveField(
            model_name='item',
            name='wished_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]

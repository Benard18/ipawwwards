# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 07:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='owner',
            new_name='developer',
        ),
    ]

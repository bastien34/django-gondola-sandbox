# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gondola_grid', '0006_auto_20170224_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gondolerow',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='gondolerow',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='gondolerow',
            name='image_3',
        ),
    ]

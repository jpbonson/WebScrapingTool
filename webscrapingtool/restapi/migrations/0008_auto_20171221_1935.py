# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-21 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_auto_20171221_0128'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('outlet', 'title', 'author')]),
        ),
    ]

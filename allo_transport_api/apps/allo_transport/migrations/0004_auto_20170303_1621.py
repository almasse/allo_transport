# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 16:21
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('allo_transport', '0003_auto_20170303_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
    ]

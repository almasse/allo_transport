# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 18:59
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('allo_transport', '0006_newspage_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='description',
        ),
        migrations.AddField(
            model_name='newspage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]

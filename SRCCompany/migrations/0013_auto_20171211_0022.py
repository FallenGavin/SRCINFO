# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-10 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRCCompany', '0012_auto_20171210_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webinfo',
            old_name='web_company',
            new_name='web_subdomain',
        ),
    ]
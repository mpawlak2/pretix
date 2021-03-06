# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0022_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='comment',
            field=models.TextField(blank=True, help_text='The text entered in this field will not be visible to the user and is available for your convenience.', verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='voucher',
            name='tag',
            field=models.CharField(blank=True, help_text='You can use this field to group multiple vouchers together. If you enter the same value for multiple vouchers, you can get statistics on how many of them have been redeemed etc.', max_length=255, verbose_name='Tag'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-08 01:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni', '0002_unapprovedmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='unapprovedmember',
            name='authorized_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unapprovedmember',
            name='date_refresh',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='unapprovedmember',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-16 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chorus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('style', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='chorus',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni.City'),
        ),
        migrations.AddField(
            model_name='chorus',
            name='conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni.Conductor'),
        ),
        migrations.AddField(
            model_name='chorus',
            name='members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumni.Member'),
        ),
    ]

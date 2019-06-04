# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-08 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KindofEarly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('article', models.TextField(verbose_name='\u6587\u7ae0')),
            ],
            options={
                'verbose_name': '\u65e9\u719f\u54c1\u79cd',
                'verbose_name_plural': '\u65e9\u719f\u54c1\u79cd',
            },
        ),
        migrations.CreateModel(
            name='KindofLate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('article', models.TextField(verbose_name='\u6587\u7ae0')),
            ],
            options={
                'verbose_name': '\u665a\u719f\u54c1\u79cd',
                'verbose_name_plural': '\u665a\u719f\u54c1\u79cd',
            },
        ),
        migrations.CreateModel(
            name='KindofMid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('article', models.TextField(verbose_name='\u6587\u7ae0')),
            ],
            options={
                'verbose_name': '\u4e2d\u719f\u54c1\u79cd',
                'verbose_name_plural': '\u4e2d\u719f\u54c1\u79cd',
            },
        ),
    ]

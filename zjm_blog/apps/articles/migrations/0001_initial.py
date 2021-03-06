# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-16 23:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False, verbose_name='分类ID')),
                ('cat_name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('parent', models.IntegerField(default=0, verbose_name='父分类ID')),
                ('is_show', models.CharField(choices=[(1, '是'), (0, '否')], default=0, max_length=1, verbose_name='是否显示')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'zjm_category',
            },
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('cat_name',)]),
        ),
    ]

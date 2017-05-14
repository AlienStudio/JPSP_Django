# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-16 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('clubid', models.CharField(max_length=4)),
                ('proprieter', models.IntegerField()),
                ('if_enroll', models.BooleanField()),
                ('enroll_group_qq', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('label', models.TextField()),
                ('state', models.BooleanField()),
                ('stars', models.IntegerField()),
                ('introduction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('ip', models.CharField(max_length=15)),
                ('comment_datetime', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=30)),
                ('send_time', models.DateField(auto_now=True)),
                ('to_user', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('nuf', '需要上传文件'), ('np', '需要发布动态'), ('pd', '动态不符合标准，无法发布'), ('ps', '动态发布成功')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('post_time', models.DateField()),
                ('add_time', models.DateField(auto_now_add=True)),
                ('edit_time', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('category', models.CharField(max_length=1)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.club')),
            ],
        ),
        migrations.CreateModel(
            name='stars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.FloatField()),
                ('star_time', models.DateField(auto_now=True)),
                ('times', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.TextField()),
                ('grade', models.IntegerField()),
                ('classroom', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.user'),
        ),
    ]

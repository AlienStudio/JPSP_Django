# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-02 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='活动名称', max_length=30)),
                ('Region', models.CharField(default='活动地点', max_length=30)),
                ('ClubName', models.CharField(default='社团', max_length=30)),
                ('Content', models.TextField(default='活动内容')),
                ('Date1', models.DateTimeField()),
                ('Date2', models.DateTimeField()),
                ('State', models.CharField(choices=[('0', 'Draft'), ('1', 'Accepted'), ('2', 'Denied')], default='0', max_length=1)),
                ('Type', models.TextField(choices=[('0', '普通'), ('1', '义卖'), ('2', '销售')], default='0')),
            ],
        ),
        migrations.CreateModel(
            name='CDUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='社团部', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassroomId', models.IntegerField()),
                ('ClubName', models.CharField(default='社团', max_length=30)),
                ('Date1', models.DateTimeField()),
                ('Date2', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClubName', models.CharField(default='社团', max_length=30)),
                ('ClubId', models.CharField(default=None, max_length=4)),
                ('ShezhangName', models.CharField(default='', max_length=8)),
                ('ShezhangQq', models.CharField(default='', max_length=20)),
                ('ShezhangGrade', models.CharField(default='', max_length=1)),
                ('ShezhangClass', models.CharField(default='', max_length=2)),
                ('IfRecruit', models.BooleanField()),
                ('EnrollGroupQq', models.CharField(default='', max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Label', models.TextField(default='')),
                ('State', models.BooleanField()),
                ('Stars', models.IntegerField(default=0)),
                ('Introduction', models.TextField(default='')),
                ('Achievements', models.TextField(default='')),
                ('Member', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=None, max_length=30)),
                ('Date', models.DateTimeField()),
                ('Region', models.CharField(default=None, max_length=30)),
                ('Content', models.TextField(default=None)),
                ('Club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club')),
            ],
        ),
        migrations.CreateModel(
            name='LostAndFound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LostOrFound', models.CharField(default='丢失', max_length=4)),
                ('LinkmanName', models.CharField(default='匿名', max_length=30)),
                ('LinkmanGrade', models.CharField(default='0', max_length=1)),
                ('LinkmanClass', models.CharField(default='0', max_length=2)),
                ('LinkmanPhoneNumber', models.CharField(default='0000000000', max_length=11)),
                ('LinkmanQq', models.CharField(default='0', max_length=20)),
                ('LostObjectName', models.CharField(default='', max_length=100)),
                ('LostPlace', models.CharField(default='', max_length=30)),
                ('Importacne', models.BooleanField(default=False)),
                ('Desc', models.TextField(default='')),
                ('LostDateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SendTime', models.DateTimeField(auto_now=True)),
                ('ToUser', models.CharField(max_length=30)),
                ('ReadTime', models.DateTimeField(default=None)),
                ('Type', models.CharField(choices=[('cps', '需要进行社团活动进行打分'), ('ca', '需要审核社团活动'), ('ce', '需要审核社团建立'), ('default', 'default')], default='default', max_length=3)),
                ('Content', models.TextField(default='')),
                ('FromUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClubName', models.CharField(default='社团', max_length=30)),
                ('LinkmanGrade', models.CharField(default='1', max_length=1)),
                ('LinkmanClass', models.CharField(default='1', max_length=2)),
                ('LinkmanName', models.CharField(default='', max_length=8)),
                ('LinkmanPhoneNumber', models.CharField(default='00000000000', max_length=11)),
                ('LinkmanQq', models.CharField(default='00000000', max_length=20)),
                ('Region', models.CharField(default='00000', max_length=30)),
                ('Date1', models.DateField(default=None)),
                ('Date2', models.TimeField(default=None)),
                ('Process', models.TextField(default='')),
                ('Content', models.TextField(default='')),
                ('Assessment', models.TextField(default='')),
                ('Feeling', models.TextField(default='')),
                ('Stars', models.FloatField(default=0.0)),
                ('StarTime', models.DateTimeField(default=None)),
                ('Pass', models.CharField(default='1', max_length=1)),
                ('CludId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='settings', max_length=10)),
                ('clubid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Token', models.CharField(default='', max_length=30)),
                ('UserType', models.CharField(choices=[('club', 'club'), ('cd', 'club_department'), ('s', 'student'), ('t', 'teacher')], default=None, max_length=4)),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(default=None, max_length=12)),
                ('Class', models.IntegerField()),
                ('Grade', models.IntegerField()),
                ('AttendYear', models.CharField(default='2016', max_length=4)),
                ('QQ', models.CharField(default=None, max_length=12)),
                ('Phone', models.CharField(default=None, max_length=12)),
                ('Email', models.EmailField(max_length=254)),
                ('UserObject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='ClubId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club'),
        ),
        migrations.AddField(
            model_name='activity',
            name='Participants',
            field=models.ManyToManyField(default=None, to='jpspapp.UserProfile'),
        ),
    ]

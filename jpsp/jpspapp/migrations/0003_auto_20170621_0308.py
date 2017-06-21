# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jpspapp', '0002_auto_20170519_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActivityName', models.CharField(default='活动名称', max_length=30)),
                ('Region', models.CharField(default='活动地点', max_length=30)),
                ('ClubName', models.CharField(default='社团', max_length=30)),
                ('Content', models.TextField(default='活动内容')),
                ('Date1', models.DateTimeField()),
                ('Date2', models.DateTimeField()),
                ('State', models.CharField(choices=[('0', 'Draft'), ('1', 'Accepted'), ('2', 'Denied')], default='0', max_length=1)),
                ('Type', models.TextField(choices=[('0', '普通'), ('1', '义卖'), ('2', '销售')], default='0')),
                ('Participants', models.TextField(default='')),
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
            name='LostAndFound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LostOrFound', models.CharField(default='丢失', max_length=4)),
                ('LinkmanName', models.CharField(default='匿名', max_length=30)),
                ('LinkmanGrade', models.CharField(default='0', max_length=1)),
                ('LinkmanClassroom', models.CharField(default='0', max_length=2)),
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
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='settings', max_length=10)),
                ('clubid', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='club',
            old_name='achievements',
            new_name='Achievements',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='if_enroll',
            new_name='IfRecruit',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='introduction',
            new_name='Introduction',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='label',
            new_name='Label',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='shezhang_name',
            new_name='ShezhangName',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='shezhang_qq',
            new_name='ShezhangQq',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='state',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='from_user',
            new_name='FromUser',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='to_user',
            new_name='ToUser',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='user',
            new_name='UserName',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='attend_year',
            new_name='AttendYear',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='classroom',
            new_name='Classroom',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='grade',
            new_name='Grade',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lftlip',
            new_name='Lftlip',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='UserName',
        ),
        migrations.RemoveField(
            model_name='club',
            name='clubid',
        ),
        migrations.RemoveField(
            model_name='club',
            name='enroll_group_qq',
        ),
        migrations.RemoveField(
            model_name='club',
            name='name',
        ),
        migrations.RemoveField(
            model_name='club',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='message',
            name='read_time',
        ),
        migrations.RemoveField(
            model_name='message',
            name='send_time',
        ),
        migrations.RemoveField(
            model_name='message',
            name='type',
        ),
        migrations.RemoveField(
            model_name='token',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='token',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='token',
            name='token',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='club',
        ),
        migrations.AddField(
            model_name='cduser',
            name='username',
            field=models.CharField(default='社团部', max_length=30),
        ),
        migrations.AddField(
            model_name='club',
            name='ClubName',
            field=models.CharField(default='社团', max_length=30),
        ),
        migrations.AddField(
            model_name='club',
            name='EnrollGroupQq',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='club',
            name='Member',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='club',
            name='ShezhangClassroom',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='club',
            name='ShezhangGrade',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AddField(
            model_name='club',
            name='Stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='ReadTime',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='message',
            name='SendTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='message',
            name='Type',
            field=models.CharField(choices=[('cps', '需要进行社团活动进行打分'), ('ca', '需要审核社团活动'), ('ce', '需要审核社团建立'), ('default', 'default')], default='default', max_length=3),
        ),
        migrations.AddField(
            model_name='post',
            name='ClubName',
            field=models.CharField(default='社团', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='CludId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club'),
        ),
        migrations.AddField(
            model_name='post',
            name='IfPass',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='token',
            name='Token',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='token',
            name='UserType',
            field=models.CharField(choices=[('club', 'club'), ('cd', 'club_department'), ('s', 'student'), ('t', 'teacher')], default=None, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='StudyID',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='classroom',
            name='ClubId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club'),
        ),
        migrations.AddField(
            model_name='activity',
            name='ClubId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jpspapp.Club'),
        ),
    ]

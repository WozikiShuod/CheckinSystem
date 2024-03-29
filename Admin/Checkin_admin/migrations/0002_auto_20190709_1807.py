# Generated by Django 2.2.3 on 2019-07-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkin_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_Class',
            field=models.CharField(default='通信1603', max_length=20, verbose_name='班级'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Classroom_Num',
            field=models.CharField(max_length=10, verbose_name='上课地点'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Course_Name',
            field=models.CharField(max_length=20, verbose_name='课程'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Email_Addr',
            field=models.EmailField(max_length=254, verbose_name='邮件'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Phone_Num',
            field=models.CharField(max_length=20, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_Checkin_status',
            field=models.CharField(max_length=5, verbose_name='签到状态'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_Checkin_time',
            field=models.DateTimeField(auto_now=True, verbose_name='签到时间'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_ID',
            field=models.IntegerField(verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_Name',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher_Name',
            field=models.CharField(max_length=10, verbose_name='教师'),
        ),
    ]

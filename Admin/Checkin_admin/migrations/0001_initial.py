# Generated by Django 2.2.3 on 2019-07-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.IntegerField()),
                ('student_Name', models.CharField(max_length=10)),
                ('student_Checkin_status', models.CharField(max_length=5)),
                ('student_Checkin_time', models.DateTimeField(auto_now=True)),
                ('Course_Name', models.CharField(max_length=20)),
                ('Classroom_Num', models.CharField(max_length=10)),
                ('teacher_Name', models.CharField(max_length=10)),
                ('Phone_Num', models.CharField(max_length=20)),
                ('Email_Addr', models.EmailField(max_length=254)),
            ],
        ),
    ]
from django.db import models


class Student(models.Model):
    student_ID = models.IntegerField(verbose_name="学号")
    student_Name = models.CharField(max_length=10, verbose_name="姓名")
    student_Class = models.CharField(max_length=20, verbose_name="班级", default='通信1603')
    student_Checkin_status = models.CharField(max_length=5, verbose_name="签到状态")
    student_Checkin_time = models.DateTimeField(auto_now=True, verbose_name="签到时间")
    Course_Name = models.CharField(max_length=20, verbose_name="课程")
    Classroom_Num = models.CharField(max_length=10, verbose_name="上课地点")
    teacher_Name = models.CharField(max_length=10, verbose_name="教师")
    Phone_Num = models.CharField(max_length=20, verbose_name="电话")
    Email_Addr = models.EmailField(verbose_name="邮件")

    def __str__(self):
        return self.student_Name
# Create your models here.

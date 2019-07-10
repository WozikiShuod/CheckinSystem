
from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_ID', 'student_Name', 'student_Class', 'student_Checkin_status', 'student_Checkin_time', 'Course_Name',
                    'Classroom_Num', 'teacher_Name', 'Phone_Num', 'Email_Addr')
    list_filter = ('student_Class', 'Course_Name')


admin.site.register(Student, StudentAdmin)

# Register your models here.

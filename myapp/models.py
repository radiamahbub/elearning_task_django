from django.db import models

# Create your models here.

class DepartmentModel(models.Model):
    department_name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    department_head = models.CharField(max_length=150, null=True)


class CourseModel(models.Model):
    course_title = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    c_image = models.ImageField(upload_to='media/course_img', null=True) 

class StudentModel(models.Model):
    student_name = models.CharField(max_length=150, null=True)
    s_image = models.ImageField(upload_to='media/student_img', null=True)
    admission_date = models.DateField(null=True)
    course_name = models.CharField(max_length=150, null=True)
    course_fee = models.IntegerField(null=True)

class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    phone_number = models.IntegerField(null=True)           

class ResultModel(models.Model):
    student_name = models.CharField(max_length=150, null=True)
    marks = models.PositiveIntegerField(null=True)
    grade = models.CharField(max_length=100, null=True)    
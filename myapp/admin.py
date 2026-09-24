from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.register(DepartmentModel)
admin.site.register(CourseModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(ResultModel)
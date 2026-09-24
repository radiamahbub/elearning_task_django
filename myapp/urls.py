from django.urls import path
from myapp.views import *


urlpatterns = [
    path('', home, name='home'),

    path('department/', department_create, name='department_create'),
    path('department_view/', department_view, name='department_view'),
    path('department_update/<str:d_id>/', department_update, name='department_update'),
    path('department_delete/<str:d_id>/', department_delete, name='department_delete'),

    path('course/', course_create, name='course_create'),
    path('course_view/', course_view, name='course_view'),
    path('course_update/<str:c_id>/', course_update, name='course_update'),
    path('course_delete/<str:c_id>/', course_delete, name='course_delete'),

    path('student/', student_create, name='student_create'),
    path('student_view/', student_view, name='student_view'),
    path('student_update/<str:s_id>/', student_update, name='student_update'),
    path('student_delete/<str:s_id>/', student_delete, name='student_delete'),

    path('teacher/', teacher_create, name='teacher_create'),
    path('teacher_view/', teacher_view, name='teacher_view'),
    path('teacher_update/<str:t_id>/', teacher_update, name='teacher_update'),
    path('teacher_delete/<str:t_id>/', teacher_delete, name='teacher_delete'),

    path('result/', result_create, name='result_create'),
    path('result_view/', result_view, name='result_view'),
    path('result_update/<str:r_id>/', result_update, name='result_update'),
    path('result_delete/<str:r_id>/', result_delete, name='result_delete'),
    

]

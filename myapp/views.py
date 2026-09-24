from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')


# ---------------Department-------------------

def department_create(request):

    if request.method == "POST":
        department_name = request.POST.get('department_name')
        description = request.POST.get('description')
        department_head = request.POST.get('department_head')

        DepartmentModel.objects.create(
            department_name = department_name,
            description = description,
            department_head = department_head
        )
        
        return redirect('department_view')

    return render(request, 'department.html')


def department_view(request):

    d_data = DepartmentModel.objects.all()

    context = {
        'd_data':d_data
    }

    return render(request, 'department_view.html', context)


def department_update(request, d_id):

    d_data = DepartmentModel.objects.get(id=d_id)

    if request.method == "POST":
            department_name = request.POST.get('department_name')
            description = request.POST.get('description')
            department_head = request.POST.get('department_head')

            d_data.department_name = department_name
            d_data.description = description
            d_data.department_head = department_head

            d_data.save()

            return redirect('department_view')

    context = {
         'd_data':d_data
    }


    return render(request, 'department_update.html', context)


def department_delete(request, d_id):

    DepartmentModel.objects.get(id=d_id).delete()

    return redirect('department_view')

#----------------Student----------------------------

def student_create(request):

    if request.method == 'POST':
            student_name = request.POST.get('student_name')
            s_image = request.FILES.get('s_image')
            admission_date = request.POST.get('admission_date')
            course_name = request.POST.get('course_name')
            course_fee = request.POST.get('course_fee')
    
            StudentModel.objects.create(
                student_name = student_name,
                s_image = s_image, 
                admission_date = admission_date, 
                course_name = course_name,
                course_fee = course_fee, 
            )
    
            return redirect('student_view')

    return render(request, 'student.html')

def student_view(request):

     s_data = StudentModel.objects.all()

     context = {
          's_data': s_data
     }

     return render(request, 'student_view.html', context)

def student_update(request, s_id):

    s_data =  StudentModel.objects.get(id=s_id)

    if request.method == 'POST':
                student_name = request.POST.get('student_name')
                s_image = request.FILES.get('s_image')
                admission_date = request.POST.get('admission_date')
                course_name = request.POST.get('course_name')
                course_fee = request.POST.get('course_fee')

                s_data.student_name = student_name
                s_data.admission_date = admission_date
                s_data.course_name = course_name
                s_data.course_fee = course_fee

                if s_image:
                    s_data.s_image = s_image

                s_data.save()

                return redirect('student_view')

    context = {
          's_data':s_data
    }   

    return render(request, 'student_update.html', context)   

def student_delete(request, s_id):
      StudentModel.objects.get(id = s_id).delete()
      return redirect('student_view')

#---------------Teacher---------------------------

def teacher_create(request):

    if request.method == 'POST':
            teacher_name = request.POST.get('teacher_name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
    
            TeacherModel.objects.create(
                teacher_name = teacher_name,
                email = email, 
                phone_number = phone_number 
            )
    
            return redirect('teacher_view')

    return render(request, 'teacher.html')

def teacher_view(request):

     t_data = TeacherModel.objects.all()

     context = {
          't_data': t_data
     }

     return render(request, 'teacher_view.html', context)

def teacher_update(request, t_id):

    t_data =  TeacherModel.objects.get(id=t_id)

    if request.method == 'POST':
                teacher_name = request.POST.get('teacher_name')
                email = request.POST.get('email')
                phone_number = request.POST.get('phone_number')

                t_data.teacher_name = teacher_name
                t_data.email = email
                t_data.phone_number = phone_number

                t_data.save()

                return redirect('teacher_view')

    context = {
          't_data':t_data
    }   

    return render(request, 'teacher_update.html', context) 

def teacher_delete(request, t_id):
      TeacherModel.objects.get(id = t_id).delete()
      return redirect('teacher_view')

#---------------Result----------------------------          

def result_create(request):

    if request.method == 'POST':
            student_name = request.POST.get('student_name')
            marks = request.POST.get('marks')
            grade = request.POST.get('grade')
    
            ResultModel.objects.create(
                student_name = student_name,
                marks = marks, 
                grade = grade, 
            )
    
            return redirect('result_view')

    return render(request, 'result.html')

def result_view(request):

     r_data = ResultModel.objects.all()

     context = {
          'r_data': r_data
     }

     return render(request, 'result_view.html', context)

def result_update(request, r_id):

    r_data =  ResultModel.objects.get(id=r_id)

    if request.method == 'POST':
                student_name = request.POST.get('student_name')
                marks = request.POST.get('marks')
                grade = request.POST.get('grade')

                r_data.student_name = student_name
                r_data.marks = marks
                r_data.grade = grade

                r_data.save()

                return redirect('result_view')

    context = {
          'r_data':r_data
    }   

    return render(request, 'result_update.html', context)   

def result_delete(request, r_id):
      ResultModel.objects.get(id = r_id).delete()
      return redirect('result_view')
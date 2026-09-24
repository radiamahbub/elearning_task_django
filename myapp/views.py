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
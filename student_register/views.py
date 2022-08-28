from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'student_register/base.html')


def student_list(request):
    return render(request, 'student_register/student_list.html')


def student_form(request):
    return render(request, 'student_register/student_form.html')

from django.shortcuts import render

# Create your views here.


def student_list(request):
    return render(request, 'student_register/base.html')

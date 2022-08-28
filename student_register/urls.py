from django.urls import path

from .views import student_form, student_list, base

urlpatterns = [
    path("", base, name="base"),
    path("list/", student_list, name='list'),
    path('form/', student_form, name='form')
]

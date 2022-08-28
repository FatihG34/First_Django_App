from dataclasses import fields
from django import forms
from .models import *


class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Full Name', 'Number',
                  'Phone Number', 'e-mail', 'Gender', 'Path']

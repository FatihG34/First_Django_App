from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    GENDER = [
        ('1', 'Female'),
        ('2', 'Male'),
        ('3', 'Other'),
        ('4', 'Prefer not to say'),
    ]
    PATH = [
        ('1', 'Full Stack'),
        ('2', 'Data Science'),
        ('3', 'DevOps'),
        ('4', 'AWS'),
        ('5', 'ITF'),
    ]
    full_name = models.CharField('Full Name', max_length=30)
    number = models.IntegerField('Number')
    mobile = PhoneNumberField('Phone Number')
    email = models.EmailField('e-mail', max_length=254)
    gender = models.CharField('Gender', max_length=30, choices=GENDER)
    path = models.CharField('Path', max_length=30, choices=PATH)

    def __str__(self):
        return f'{self.number} - {self.full_name}'

    class Meta:
        ordering = ['number']

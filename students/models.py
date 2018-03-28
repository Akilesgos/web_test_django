from django.db import models
from django.conf import settings 
from courses.models import Course



class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    date_of_birth = models.DateField(help_text='Write yours date ofbirth')
    email = models.EmailField(unique=True, max_length=64,
                             help_text='Write yours email')
    phone = models.CharField(unique=True, help_text='Write yours phone',
                             max_length=12)
    address = models.CharField(help_text='Write yours adress',
                               max_length=244, null=True,)
    skype = models.CharField(help_text='Write yours skype',
                             max_length=64, null=True,blank = True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return(self.name)
    
# Create your models here.

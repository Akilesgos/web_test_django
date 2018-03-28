from django.shortcuts import render
from courses import models
from students.models import Student


def students_list(request, id):
    course = models.Course.objects.get(id=id)
    student_information = Student.objects.filter(courses=course)
    return render(request, 'students/students.html',
                  {'student_information': student_information})


def students_all_list(request):
    student_all = Student.objects.all()
    return render(request, 'students/students_all.html',
                  {'student_all': student_all})


def students_id(request, id):
    student_personal = Student.objects.filter(id=id)
    return render(request, 'students/students_person.html',
                  {'student_personal': student_personal})


# Create your views here.

'''
    number = int(id)
    if number == 1:
        course = models.Course.objects.get(id=1)
        student_information = Student.objects.filter(courses=course)
    elif number == 2:
        course = models.Course.objects.get(id=2)
        student_information = Student.objects.filter(courses=course)
    elif number == 3:
        course = models.Course.objects.get(id=3)
        student_information = Student.objects.filter(courses=course)
'''
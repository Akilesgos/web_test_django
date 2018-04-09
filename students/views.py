from django.shortcuts import render, redirect
from students.models import Student
from django.urls import reverse
from django.contrib import messages
from students.utils import detail_view
from courses import models
from .forms import StudentModelForm


def students_list(request, id):
    course = models.Course.objects.get(id=id)
    student_information = Student.objects.filter(courses=course)
    return render(request, 'students/students.html',
                  {'student_information': student_information})


def students_all_list(request):
    student_all = Student.objects.all()
    return render(request, 'students/students_all.html',
                  {'student_all': student_all})


def students_id(request, pk):
    return detail_view(request, pk, Student)


def add_student(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Saved!")
            return redirect(reverse('students:edit_student',
                                    args=[instance.id]))
    else:
        form = StudentModelForm(initial={'courses': 'assa'})
    return render(request, 'students/add_student_form.html', {'form': form})


def edit_student(request, pk):
    student_edit = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student_edit)
        if form.is_valid():
            student_edit = form.save()
            messages.success(request, 'Your profile was edit.')
            return redirect(reverse('students:students_all'))
    else:
        form = StudentModelForm(instance=student_edit)
    return render(request, 'students/add_student_form.html', {'form': form})


def delete_student(request, pk):
    delete_student = Student.objects.get(id=pk)
    if request.method == 'POST':
        delete_student.save()
        messages.success(request, 'Your profile was delete.')
        return redirect(reverse('students:students_all'))
    return render(request, 'students/delete_student.html',
                  {'delete_student': delete_student})
# Create your views here.

'''
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Saved!")
            return redirect(reverse('courses:edit_courses', args=[instance.id]))
    else:
        form = StudentModelForm(initial={'name': 'Akio the Beast'})
        
        
        
def students_id(request, student_id):
    student_personal = Student.objects.filter(id=student_id)
    return render(request, 'students/detail.html',
                  {'student_personal': student_personal})
                  
                  
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
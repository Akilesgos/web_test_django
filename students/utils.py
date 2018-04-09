from django.shortcuts import render, get_object_or_404


def detail_view(request, pk, obj_class):
    obj_name = obj_class.__name__.lower()
    print(obj_name)
    obj = get_object_or_404(obj_class, id=pk)
    return render(request, '%ss/detail.html' % obj_name, {obj_name:obj})


def list_view(request, pk, obj_class, obj_class_2):
    obj_name = obj_class.__name__.lower()
    print(obj_name)
    obj = get_object_or_404(obj_class, id=pk)
    disease = get_object_or_404(obj_class_2, pk=disease_id)
    print(obj)
    return render(request, '%ss/detail.html' % obj_name, {obj_name:obj})

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
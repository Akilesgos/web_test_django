from django.shortcuts import render
from courses.models import Course, Lesson


def my_decorator_for_the_courses(function):
    def the_wrapper_for_the_courses(request, indification_number):
        function(request, indification_number)
        number = int(indification_number)
        if number == 1:
            course = Course.objects.get(id=1)
            lessons = Lesson.objects.filter(course=course)  # filtration in
            # foreing
        elif number == 2:
            course = Course.objects.get(id=2)
            lessons = Lesson.objects.filter(course=course)  # filtration in foreing
        elif number == 3:
            course = Course.objects.get(id=3)
            lessons = Lesson.objects.filter(course=course)  # filtration in foreing
        return render(request, 'courses/detail.html', {'course': course,
                                                    'lessons': lessons})
    return the_wrapper_for_the_courses


# Create your views here.

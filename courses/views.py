from django.shortcuts import render
from django.views import generic
from courses.models import Course, Lesson
from courses.logic_for_views import my_decorator_for_the_courses


def index(request):
    course = Course.objects.all()
    return render(request, 'courses/index.html', {'course': course})


def contacts(request):
    return render(request, 'courses/contacts.html',)


@my_decorator_for_the_courses
def courses(request, indification_number):
    return

# Create your views here.

'''
def courses(request, indification_number):
    int_number_page = int(indification_number)
    if int_number_page == 1:
        course = Course.objects.get(id=1)
        lessons = Lesson.objects.filter(course=course)  # filtration in foreing
    #  key
    elif int_number_page == 2:
        course = Course.objects.get(id=2)
        lessons = Lesson.objects.filter(course=course)  # filtration in
# foreingkey
    elif int_number_page == 3:
        course = Course.objects.get(id=3)
        lessons = Lesson.objects.filter(course=course)  # filtration in
        # foreing key
    return render(request, 'courses/courses.html', {'course': course,
                                                 'lessons': lessons})                                      
def index(request):
latest_question_list = Question.objects.order_by('-pub_date')[:5]
content = {
'latest_question_list': latest_question_list,
}
return render(request, 'polls/index.html', content)

class IndexView(generic.ListView):
template_name = 'polls/index.html'
context_object_name = 'latest_question_list'
def get_queryset(self):
""Return the last five published questions."""
return Question.objects.order_by('-pub_date')[:5]
'''
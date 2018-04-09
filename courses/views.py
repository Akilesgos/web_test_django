from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm


def index(request):
    course = Course.objects.all()
    return render(request, 'courses/index.html', {'course': course})


def contacts(request):
    return render(request, 'courses/contacts.html', )


def courses(request, pk):
    course = get_object_or_404(Course, id=pk)
    lessons = Lesson.objects.filter(course=course)  # filtration in
    return render(request, 'courses/detail.html', {'course': course,
                                                   'lessons': lessons})


def add_view_course(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Saved!")
            return redirect(
                reverse('courses:edit_courses', args=[instance.id]))
    else:
        form = CourseModelForm(initial={'coach': 'Akio the Beast'})
    return render(request, 'courses/add_form.html', {'form': form})


def edit_view_course(request, pk):  # now you could edit this form
    course_edit = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course_edit)
        if form.is_valid():
            course_edit = form.save()
            messages.success(request, 'Your profile was edit.')
            return redirect(reverse('courses:main'))
    else:
        form = CourseModelForm(instance=course_edit)
    return render(request, 'courses/edit_course.html', {'form': form})


def delete_course(request, pk):
    course_delete = Course.objects.get(id=pk)
    if request.method == 'POST':
        course_delete.delete()
        messages.success(request, 'Your {} deleted.'.format(
            course_delete.name))
        return redirect('/courses/add_lesson')
    return render(request, 'courses/delete_course.html',
                  {'course_delete': course_delete})


def add_view_lesson(request):
    #  model_form=CourseModelForm(initial={'coach':'Akio the Beast'}) dont need
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Your lesson was added.')
            return redirect(reverse('courses:edit_lesson', args=[instance.id]))
    else:
        form = LessonModelForm()
    return render(request, 'courses/add_lesson.html', {'form': form})


def edit_lesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    course = Course.objects.get(lesson=lesson)
    if request.method == 'POST':
        form = LessonModelForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Your lesson was eddit.')
            return redirect(reverse('courses:courses', args=[course.id]))
    else:
        form = LessonModelForm(instance=lesson)
        return render(request, 'courses/edit_lesson.html', {'form': form})


def delete_lesson(request, pk):
    lesson_delete = Lesson.objects.get(id=pk)
    course = Course.objects.get(lesson=lesson_delete)
    if request.method == 'POST':
        lesson_delete.delete()
        messages.success(request, 'Your {} deleted.'.format(
            lesson_delete.subject))
        return redirect(reverse('courses:courses', args=[course.id]))
    return render(request, 'courses/delete_lesson.html',
                  {'lesson_delete': lesson_delete})


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
    return render(request, 'courses/detail.html', {'course': course,
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

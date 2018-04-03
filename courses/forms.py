from django.forms import ModelForm
from .models import Course, Lesson
from django.forms import Textarea


class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['subject', 'description', 'course', 'order' ]


class CourseModelForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'coach', 'assistant', 'description']
        #widgets = {'coach': Textarea(attrs={'cols': 20, 'rows': 1})}
        labels = {'description': 'Description'}

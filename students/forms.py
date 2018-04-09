from django.forms import ModelForm
from .models import Student


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'email', 'date_of_birth', 'phone',
                  'courses',]



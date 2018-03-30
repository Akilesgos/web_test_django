from django.urls import path
from courses.views import courses, index, contacts


app_name = 'courses'


urlpatterns = [
    path('', index, name='main'),
    path('contacts', contacts, name='contacts'),
    path('courses/<int:indification_number>/', courses, name='courses'),
    ]

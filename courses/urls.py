from django.urls import path
from courses.views import courses, index


urlpatterns = [
    path('', index, name='main'),
    path('courses/<int:indification_number>/', courses, name='courses'),
    ]

"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.urls import include
from students.views import students_list, students_all_list, students_id

# from instructors.views import hello,hello_http, views_about_course,views_student, views_student_detail, instructors_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('students/', include('students.urls', namespace='students')),
    path('coaches/', include('coaches.urls', namespace='coaches')),
]



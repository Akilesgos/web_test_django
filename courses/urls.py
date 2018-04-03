from django.urls import path
from courses import views


app_name = 'courses'

urlpatterns = [
    path('', views.index, name='main'),
    path('contacts', views.contacts, name='contacts'),
    path('courses/<int:pk>/', views.courses, name='courses'),
    path('courses/add', views.add_view_course, name='add_courses'),
    path('courses/edit/<int:pk>/', views.edit_view_course, name='edit_courses'),
    path('courses/delete/<int:pk>/', views.delete_course, name='delete_courses'),
    path('courses/add_lesson', views.add_view_lesson, name='add_lesson'),
    path('courses/edit_lesson/<int:pk>', views.edit_lesson, name='edit_lesson'),
    path('courses/delete_lesson/<int:pk>', views.delete_lesson,
         name='delete_lesson'),
    ]

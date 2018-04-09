from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    path('', views.students_all_list, name='students_all'),
    path('<int:pk>/', views.students_id, name='students_id'),
    path('course_id=<int:id>', views.students_list,
         name='students_list_course_id'),
    path('add', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    ]

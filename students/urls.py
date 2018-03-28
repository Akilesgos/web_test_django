from django.urls import path
from students.views import students_list, students_all_list, students_id


app_name = 'students'


urlpatterns = [
    path('', students_all_list, name='students_all'),
    path('<int:id>/', students_id, name='students_id'),
    path('course_id=<int:id>', students_list,
         name='students_list_course_id'),
]



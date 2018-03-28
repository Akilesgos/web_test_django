from django.urls import path
from coaches.views import personal_teacher


app_name = 'coaches'


urlpatterns = [
    path('<int:id>', personal_teacher, name='coaches_personal'),
    ]




from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course, Lesson


def personal_teacher(request, id):
    teacher = Coach.objects.filter(id=id)
    id_teacher = Coach.objects.get(id=id)
    coach = Course.objects.filter(coach=id_teacher)
    assistant = Course.objects.filter(assistant=id_teacher)
    return render(request, 'coaches/coaches_person.html', {'teacher':teacher,
                                                       'coach':coach,
                                                       'assistant':assistant})

# Create your views here.

'''
    <h1>{{teacher.first_name}}</h1>
  </div>
  <div>      
    <table class="table table-striped">
        <tbody>
          <tr>
            <td>Дата Рождения</td>
            <td>{{teacher.date_of_birth}}</td>
          </tr>
          <tr>
            <td>Адресс</td>
            <td>{{teacher.address}}</td>
        </tr>
         <tr>
            <td>Почта</td>
            <td>{{teacher.email}}</td>
        <tr>
            <td>Логин Скайп</td>
            <td>{{teacher.skype}}</td>
        </tr>
         <tr>
            <td>Телефон</td>
            <td>{{teacher.phone}}</td>
         </tr>
            <td>Курсы учитель</td>
          {%for id in course%}
            <td>{{id}}</td>
          {%endfor%}
         </tr>
            <td>Курсы асистент </td>
          {%for id in course%}
            <td>{{id.assistant.}}</td>
          {%endfor%}
        <tr>

'''
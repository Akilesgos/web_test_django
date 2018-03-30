from django.contrib import admin
from coaches.models import Coach
from courses.models import Course, Lesson


class CourseInline(admin.TabularInline):
    model = Course
    fk_name = 'assistant'


class AsistentInLine(admin.TabularInline):
    model = Course
    fk_name = 'coach'


class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description',)
    list_filter = ['is_staff']
    exclude = ['date_of_birth', 'password', 'last_login',
               'groups', 'user_permissions']
    inlines = [CourseInline, AsistentInLine]


admin.site.register(Coach, CoachAdmin)

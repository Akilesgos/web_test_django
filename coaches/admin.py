from django.contrib import admin
from coaches.models import Coach
from courses.models import Course, Lesson


class CourseInline(admin.TabularInline):
    model = Course
    fk_name = 'assistant'

class AsistentInline(admin.TabularInline):
    model = Course
    fk_name = 'coach'

class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description',)
    list_filter = ['is_staff']
    exclude = ['date_of_birth', 'first_name', 'password', 'last_login',
               'groups', 'user_permissions']
    inlines = [CourseInline,AsistentInline]


admin.site.register(Coach, CoachAdmin)

'''
it works

class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description',)
    list_filter = ['is_staff']
    
# unregister old user admin

# register new user admin
admin.site.register(Coach, CoachAdmin)
'''
# Register your models here.
'''
class UserInline(admin.StackedInline):
    model = AuthUserAdmin

class UserInline(admin.StackedInline):
    model = User

class UserAdmin(admin.ModelAdmin):
    inlines = [UserInline]
    
class CoachAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'skype', 'description',)
    list_filter = ['user']
    inlines = [AuthUserAdmin]

admin.site.register(Coach, CoachAdmin)


class UserInline(admin.StackedInline):
    model = User
    fields = ['is_staff']
class CoachInline(admin.StackedInline):
    model = Coach

class UserInline(admin.StackedInline):
    model = User

class UserAdmin(admin.ModelAdmin):
    inlines = (StudentInline, TeacherInline)

    
'''
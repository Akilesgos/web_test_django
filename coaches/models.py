from django.db import models
from django.contrib.auth.models import User


class Coach(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                parent_link=True, )
    date_of_birth = models.DateField('date of birth', null=True,
                                    blank=True)
    gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f',
                                                                     'Famale')))
    phone = models.CharField(max_length=64,
                             help_text='Write your mobile number', )
    address = models.CharField(max_length=128,
                               help_text='Write your address ',
                               null=True,
                               blank=True)
    skype = models.CharField(max_length=64,
                             help_text='Write your skype number',
                             null=True,
                             blank=True)
    description = models.TextField(help_text='Full description of the course',
                                   max_length=255,
                                   null=True,
                                   blank=True)

    def __unicode__(self):
        return unicode(self.user)


'''
class Coach(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                parent_link=True)

    date_of_birth = models.DateField('date of birth')
    gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f',
                                                                     'Famale')))
    phone = models.CharField(max_length=64,
                             help_text='Write your mobile number', )
    address = models.CharField(max_length=128,
                               help_text='Write your address ',
                               null=True,
                               blank=True)
    skype = models.CharField(max_length=64,
                             help_text='Write your skype number',
                             null=True,
                             blank=True)
    description = models.TextField(help_text='Full description of the course',
                                   max_length=255,
                                   null=True,
                                   blank=True)

    def __unicode__(self):
        return unicode(self.user)
'''
# Create your models here.

#models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, )
'''
class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

class Coach(User): наследование
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                parent_link=True)

    date_of_birth = models.DateField('date of birth')
    gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f',
                                                                     'Famale')))
    phone = models.CharField(max_length=64,
                             help_text='Write your mobile number', )
    address = models.CharField(max_length=128,
                               help_text='Write your address ',
                               null=True,
                               blank=True)
    skype = models.CharField(max_length=64,
                             help_text='Write your skype number',
                             null=True,
                             blank=True)
    description = models.TextField(help_text='Full description of the course',
                                   max_length=255,
                                   null=True,
                                   blank=True)

    def __unicode__(self):
        return unicode(self.user)
'''
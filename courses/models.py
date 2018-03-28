from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name='Name of the course', max_length=64)
    short_description = models.CharField(max_length=122,
                                         help_text='Short description ofthe course',
                                         null=True,
                                         blank=True)
    description = models.TextField(help_text='Full description of the course',
                                   max_length=255,
                                   null=True,
                                   blank=True)
    coach = models.ForeignKey('coaches.Coach', on_delete=models.CASCADE,
                              related_name='coach_courses',
                              null=True,
                              blank=True)
    assistant = models.ForeignKey('coaches.Coach', on_delete=models.CASCADE,
                                  related_name='assistants_courses',
                                  null=True,
                                  blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(verbose_name='Subject',
                               max_length=64,
                               help_text='Subject')
    description = models.TextField(max_length=255,
                                   help_text='description of the Subject',
                                   null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, )
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

# Create your models here.

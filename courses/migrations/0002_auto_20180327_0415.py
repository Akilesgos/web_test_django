# Generated by Django 2.0.3 on 2018-03-27 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assistants_courses', to='coaches.Coach'),
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_courses', to='coaches.Coach'),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.CharField(blank=True, help_text='Short description ofthe course', max_length=122, null=True),
        ),
    ]

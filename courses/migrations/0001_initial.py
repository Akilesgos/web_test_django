# Generated by Django 2.0.3 on 2018-03-22 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name of the course')),
                ('short_description', models.CharField(blank=True, help_text='Short description of the course', max_length=122, null=True)),
                ('description', models.TextField(blank=True, help_text='Full description of the course', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='Subject', max_length=64, verbose_name='Subject')),
                ('description', models.TextField(blank=True, help_text='description of the Subject', max_length=255, null=True)),
                ('order', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
    ]

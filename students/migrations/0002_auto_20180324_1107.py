# Generated by Django 2.0.3 on 2018-03-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(help_text='Write yours adress', max_length=244, null=True),
        ),
    ]

# Generated by Django 3.2.16 on 2022-10-15 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_studentintutorcourse_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]

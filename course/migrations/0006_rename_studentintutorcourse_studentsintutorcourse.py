# Generated by Django 3.2.16 on 2022-10-15 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_course'),
        ('tutor', '0001_initial'),
        ('course', '0005_remove_course_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentInTutorCourse',
            new_name='StudentsInTutorCourse',
        ),
    ]
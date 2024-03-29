# Generated by Django 4.1.2 on 2022-10-24 00:33

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
        ('tutor', '0001_initial'),
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_tutor', to='tutor.tutor'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='course',
            field=auto_prefetch.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_users', to='course.course'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='student_tutor_course', to='student.student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='tasks',
            field=models.ManyToManyField(blank=True, related_name='course_tasks', to='task.task'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='tutor',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_tutor_course', to='tutor.tutor'),
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together={('tutor', 'course')},
        ),
    ]

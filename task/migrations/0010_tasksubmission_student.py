# Generated by Django 3.2.16 on 2022-10-28 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('task', '0009_alter_tasksubmission_mark_earned'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksubmission',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-26 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_tasksubmission_mark_earned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksubmission',
            name='task_file',
            field=models.FileField(blank=True, upload_to='task_file/'),
        ),
        migrations.AlterField(
            model_name='tasksubmission',
            name='tasks',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
    ]
# Generated by Django 3.2.16 on 2022-10-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20221017_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Prefer Not To Say', 'Prefer Not To Say')], max_length=20, null=True),
        ),
    ]

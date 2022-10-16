# Generated by Django 3.2.16 on 2022-10-16 03:10

from django.db import migrations
import django_resized.forms
import equestlms.utils.media


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[1920, 1080], upload_to=equestlms.utils.media.MediaHelper.get_image_upload_path, verbose_name='Profile Picture'),
        ),
    ]

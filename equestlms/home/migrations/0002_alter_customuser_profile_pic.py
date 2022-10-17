# Generated by Django 4.1.2 on 2022-10-15 06:50

from django.db import migrations
import django_resized.forms
import equestlms.utils.media


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format=None,
                keep_meta=True,
                null=True,
                quality=-1,
                scale=None,
                size=[1920, 1080],
                upload_to=equestlms.utils.media.MediaHelper.get_image_upload_path,
                verbose_name="Profile Picture",
            ),
        ),
    ]

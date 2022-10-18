from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from equestlms.home.models import CustomUser
from student.models import Student
from tutor.models import Tutor


@receiver(post_save, sender=CustomUser)
def delete_student_if_made_staff(sender, instance, **kwargs):
    """
    Deletes the user from the student database

    """
    if instance.is_staff is True and instance.is_superuser is False:
        try:
            tutor = get_object_or_404(Tutor, user_id=instance.pk)
            # instance
            is_student = Student.objects.filter(user_id=tutor.user_id)
            if is_student:
                is_student.delete()
        except IntegrityError:
            pass


@receiver(post_save, sender=CustomUser)
def add_new_user_to_student(sender, instance, **kwargs):
    """
    Assumes that the new user is a student and then goes ahead
    add the new user to the student table

    """
    if (
        instance.is_new is True
        and instance.is_superuser is False
        and instance.is_staff is False
    ):
        # Check to see if the user is new or is being updated
        # if user is new then create, skip if otherwise
        try:
            Student.objects.create(user_id=instance.pk)
            instance.is_new = False
            instance.save()
        except IntegrityError:
            pass

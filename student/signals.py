from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from equestlms.home.models import CustomUser
from student.models import Student


@receiver(pre_save, sender=CustomUser)
def is_new_user(sender, instance, **kwargs):
    """
    Assumes that the new user is a student and then goes ahead
    add the new user to the student table

    """
    # Check to see if the user is new or is being updated
    if get_object_or_404(Student, user_id=instance.user_id) is not None:
        return True


@receiver(post_save, sender=CustomUser)
def add_new_user_to_student(sender, instance, **kwargs):
    """
    Assumes that the new user is a student and then goes ahead
    add the new user to the student table

    """
    # Check to see if the user is new or is being updated
    if is_new_user():
        Student.objects.create(user_id=instance.pk)

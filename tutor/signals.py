from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from equestlms.home.models import CustomUser
from student.models import Student
from tutor.models import Tutor


@receiver(post_save, sender=CustomUser)
def add_staff_user_to_tutor(sender, instance, **kwargs):
    """
    Adds the new user to tutors if is_staff == True

    """
    if instance.is_staff is True:
        new_tutor = Tutor.objects.create(user_id=instance.pk)

        # Delete the teacher from student table
        is_student = get_object_or_404(Student, user_id=new_tutor.user_id)
        if is_student:
            Student.objects.delete(user_id=is_student.user_id)

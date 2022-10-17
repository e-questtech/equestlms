from django.db import IntegrityError, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from equestlms.home.models import CustomUser
from tutor.models import Tutor


@receiver(post_save, sender=CustomUser)
def add_staff_user_to_tutor(sender, instance, **kwargs):
    """
    Adds the new user to tutors if is_staff == True

    """
    if instance.is_staff is True and instance.is_superuser is False:
        try:
            with transaction.atomic():
                Tutor.objects.create(user_id=instance.pk)

                # Delete the teacher from student table
                # is_student = get_object_or_404(Student, user_id=new_tutor.user_id)
                # if is_student:
                #     Student.objects.filter(user_id=is_student.user_id).delete()
        except IntegrityError:
            pass

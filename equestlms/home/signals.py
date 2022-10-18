from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from equestlms.home.models import CustomUser
from tutor.models import Tutor


@receiver(post_save, sender=Tutor)
def update_new_tutor_to_staff(sender, instance, **kwargs):
    """
    Update the new tutor to staff
    """
    if instance.user.is_new:
        try:
            tutor = get_object_or_404(CustomUser, pk=instance.user_id)
            tutor.is_staff = True
            tutor.save()
        except IntegrityError:
            pass

    # try:
    #     with transaction.atomic():
    #         Student.objects.filter(user_id=instance.user_id).delete()

    # except IntegrityError:
    #     pass

import auto_prefetch
from django.db import models

from equestlms.home.models import CustomUser
from equestlms.utils.models import TimeBasedModel


class Tutor(TimeBasedModel):
    user = auto_prefetch.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="Tutor"
    )
    bio = models.CharField(max_length=100)
    about = models.TextField()
    # class_students = models.ManyToManyField(Student, through="StudentsInClass")

    def __str__(self):
        return self.user.get_full_name()

import auto_prefetch
from django.db import models

from equestlms.home.models import CustomUser
from equestlms.utils.models import TimeBasedModel


class Student(TimeBasedModel):
    class StudentsEnrolled(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(enrolled=True)

    user = auto_prefetch.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="Student"
    )
    birthday = models.DateField()
    is_enrolled = models.BooleanField(default=False)
    course = models.ManyToManyField("course.Course", blank=True)

    # TODO: Change the model manager is_enrolled to enrolled
    # enrolled = StudentsEnrolled()
    objects = models.Manager()

    def __str__(self):
        return self.user.get_full_name()

    # def save(self, *args, **kwargs):

    #     super().save()
    #     if self.course is not None:
    #         StudentsInTutorCourse.objects.get(
    #             course_id=1).student.add(self.user)

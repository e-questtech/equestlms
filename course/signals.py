from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from course.models import StudentsInTutorCourse
from task.models import Task


@receiver(post_save, sender=Task)
def update_course_assignment(sender, instance, **kwargs):
    """
    Executed when a task is saved

    """
    course = get_object_or_404(StudentsInTutorCourse, course_id=instance.course.id)
    course.task.add(get_object_or_404(Task, id=instance.id))


# @receiver(post_save, sender=Task)
# def add_student_to_course(sender, instance, **kwargs):
#     """
#     Executed when a task is saved

#     """
#     course = get_object_or_404(StudentsInTutorCourse, course_id=instance.course.id)
#     course.task.add(get_object_or_404(Task, id=instance.id))
#     # course.task.save()

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from course.models import ClassRoom, Course
from student.models import Student
from task.models import Task


@receiver(post_save, sender=Course)
def create_new_course_classroom(sender, instance, **kwargs):

    if instance.is_new is True:
        ClassRoom.objects.create(
            tutor=instance.tutors, course=Course.objects.get(slug=instance.slug)
        )
        instance.is_new = False
        instance.save()


@receiver(post_save, sender=Task)
def update_course_assignment(sender, instance, **kwargs):
    """
    Executed when a task is saved
    """
    classroom = ClassRoom.objects.filter(course_id=instance.course.id)
    for course in classroom:
        course.tasks.add(get_object_or_404(Task, id=instance.id))


@receiver(post_save, sender=Student)
def add_student_to_course(sender, instance, **kwargs):
    """
    Adds the student to a class
    """
    # if enrolled skip else add the student to specified course
    if instance.is_enrolled is False:
        try:
            course = get_object_or_404(ClassRoom, course_id=instance.course.id)
            course.student.add(get_object_or_404(Student, id=instance.user_id))

            # turn enrolled flag on after updating
            instance.is_enrolled = True
            instance.save()
        except AttributeError:
            pass


# @receiver(post_save, sender=Student)
# def add_tutor_to_course(sender, instance, **kwargs):
#     """
#     Adds the student to a class
#     """
#     # if enrolled skip else add the student to specified course
#     if instance.is_enrolled is False:
#         course = get_object_or_404(ClassRoom, course_id=instance.course.id)
#         course.student.add(get_object_or_404(Student, id=instance.user_id))

#         # turn enrolled flag on after updating
#         instance.is_enrolled = True
#         instance.save()

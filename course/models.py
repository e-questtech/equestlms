import uuid

import auto_prefetch
from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import striptags, truncatechars
from django.urls import reverse
from django.utils.text import slugify

from equestlms.utils.models import TimeBasedModel


class Course(TimeBasedModel):
    """
    The top tier model of the project:
    Every Course has different topics and each topics have several lessons
    """

    title = models.CharField(max_length=125, help_text="Title of the course")
    slug = models.SlugField(max_length=125, blank=True, null=True)
    overview = RichTextField()
    cover_image = models.ImageField(upload_to="./courses_cover_images/")
    price = models.PositiveIntegerField(
        default=0,
    )
    tutors = models.ForeignKey(
        "tutor.Tutor", on_delete=models.CASCADE, related_name="course_tutor"
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        uuid_start = str(uuid.uuid1()).split("-", 1)[0]
        if not self.pk:
            self.slug = slugify(self.title) + "-" + uuid_start

        super().save()
        StudentsInTutorCourse.objects.create(
            tutor=self.tutors, course=Course.objects.get(slug=self.slug)
        )

    def get_absolute_url(self):
        return reverse("course:course-detail", kwargs={"slug": self.slug})

    @property
    def total_students(self):
        return self.students.count()

    @property
    def total_tutors(self):
        return self.tutors.count()

    @property
    def tutor_courses_count(self):
        return Course.objects.filter(tutors=self.tutors).count()

    @property
    def student_courses_count(self):
        return StudentsInTutorCourse.objects.filter(
            student__course__slug=self.slug
        ).count()

    @property
    def preview(self):
        """
        Sneak preview of the overview
        """
        cleaned_preview = striptags(self.overview)
        return truncatechars(cleaned_preview, 50)

    @property
    def duration_as_weeks(self):
        """
        The duration of the course measured by
        the difference between the start_date and end_date
        Returns the duration as number of weeks
        """
        # Get the total number of seconds between the duration
        date_difference = self.end_date - self.start_date
        date_in_seconds = date_difference.total_seconds()
        # Divide result by total seconds in a week, to get number of weeks
        date_in_weeks = date_in_seconds // (3600 * 24 * 7)
        return int(date_in_weeks)


class StudentsInTutorCourse(TimeBasedModel):
    student = models.ManyToManyField(
        "student.Student", blank=True, related_name="student_tutor_course"
    )
    tutor = auto_prefetch.ForeignKey(
        "tutor.Tutor", on_delete=models.CASCADE, related_name="student_tutor_course"
    )
    course = auto_prefetch.ForeignKey(
        Course, default=1, on_delete=models.CASCADE, related_name="course_users"
    )

    class Meta:
        unique_together = ("tutor", "course")

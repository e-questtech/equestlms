import uuid

import auto_prefetch
from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import striptags, truncatechars
from django.urls import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField

from equestlms.utils.choices import COURSE_LEVEL
from equestlms.utils.models import TimeBasedModel


class CourseCategory(models.Model):

    title = models.CharField(max_length=100)
    level = models.CharField(
        max_length=50, choices=COURSE_LEVEL, default=COURSE_LEVEL[0][0]
    )
    cover_image = ResizedImageField(quality=100)
    is_top = models.BooleanField(default=False)
    courses = models.ManyToManyField("course.Course", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home:courses", kwargs={"slug": self.title})

    def get_all_courses(self):
        courses_in_category = Course.objects.filter(category=self.title)
        return courses_in_category


class Course(TimeBasedModel):
    """
    The top tier model of the project:
    Every Course has different topics and each topics have several lessons
    """

    title = models.CharField(max_length=125, help_text="Title of the course")
    category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, default=1
    )  # Remove thhe default in develop branch
    slug = models.SlugField(max_length=125, blank=True, null=True)
    overview = RichTextField()
    cover_image = models.ImageField(upload_to="./courses_cover_images/")
    price = models.PositiveIntegerField(
        default=0,
    )
    tutor = models.ForeignKey(
        "tutor.Tutor",
        on_delete=models.CASCADE,
        related_name="course_tutor",
        null=True,
        blank=True,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_new = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    hours_per_class = models.PositiveSmallIntegerField(default=2)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        uuid_start = str(uuid.uuid1()).split("-", 1)[0]
        if not self.pk:
            self.slug = slugify(self.title) + "-" + uuid_start

        super().save()

    def get_absolute_url(self):
        return reverse("course:course-detail", kwargs={"slug": self.slug})

    @property
    def tutor_courses_count(self):
        return Course.objects.filter(tutors=self.tutors).count()

    @property
    def student_courses_count(self):
        return ClassRoom.objects.filter(student__course__slug=self.slug).count()

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


class ClassRoom(TimeBasedModel):
    student = models.ManyToManyField(
        "student.Student", blank=True, related_name="student_tutor_course"
    )
    tutor = auto_prefetch.ForeignKey(
        "tutor.Tutor",
        on_delete=models.CASCADE,
        related_name="student_tutor_course",
        null=True,
        blank=True,
    )
    course = auto_prefetch.ForeignKey(
        Course,
        default=1,
        on_delete=models.CASCADE,
        related_name="course_users",
        null=True,
        blank=True,
    )
    tasks = models.ManyToManyField(
        "task.Task",
        related_name="course_tasks",
        blank=True,
    )

    class Meta:
        unique_together = ("tutor", "course")

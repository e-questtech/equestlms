import uuid

import auto_prefetch
from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import striptags, truncatechars
from django.urls import reverse
from django.utils.text import slugify

from equestlms.utils.choices import TASKCHOICES
from equestlms.utils.models import TimeBasedModel


class Task(TimeBasedModel):
    """
    Assignments created by tutor
    """

    title = models.CharField(max_length=125, help_text="Title of the course")
    slug = models.SlugField(max_length=125, blank=True, null=True)
    content = RichTextField()
    status = models.CharField(
        choices=TASKCHOICES, default=TASKCHOICES[0][0], max_length=10
    )
    task_file = models.FileField(null=True, blank=True, upload_to="tasks/")
    course = auto_prefetch.ForeignKey(
        "course.Course", on_delete=models.CASCADE, related_name="course_task"
    )
    due_date = models.DateField()

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        uuid_start = str(uuid.uuid1()).split("-", 1)[0]
        if not self.pk:
            self.slug = slugify(self.title) + "-" + uuid_start
        super().save()

    def get_absolute_url(self):
        return reverse("task:task_detail", kwargs={"slug": self.slug})

    @property
    def tutor_assignment_count(self):
        return self.tutors.count()

    @property
    def preview(self):
        """
        Sneak preview of the overview
        """
        cleaned_preview = striptags(self.content)
        return truncatechars(cleaned_preview, 50)

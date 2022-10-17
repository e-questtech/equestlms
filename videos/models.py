from django.db import models

from equestlms.utils.models import TimeBasedModel


class Video(TimeBasedModel):
    title = models.CharField(max_length=500)
    alt_image = models.ImageField(
        upload_to="video_cover_image/",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    url = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title

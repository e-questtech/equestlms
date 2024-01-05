from django.db import models
from django.utils.text import slugify
from equestlms.utils.models import TimeBasedModel

class Category(TimeBasedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=125, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
        
class Tags(TimeBasedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Video(TimeBasedModel):
    title = models.CharField(max_length=500)
    alt_image = models.ImageField(
        upload_to="video_cover_image/",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    url = models.CharField(max_length=500)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tags, default=None, blank=True)

    def __str__(self) -> str:
        return self.title

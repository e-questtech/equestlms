from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify

from equestlms.home.models import CustomUser
from equestlms.utils.models import TimeBasedModel


class Category(TimeBasedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tags(TimeBasedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(TimeBasedModel):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=125, blank=True, null=True)
    tags = models.ManyToManyField(Tags, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to="blog_img/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

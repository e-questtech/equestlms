from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField

from equestlms.home.models import CustomUser
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


class Blog(TimeBasedModel):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=125, blank=True, null=True)
    tags = models.ManyToManyField(Tags)
    description = RichTextField()
    image = ResizedImageField(size=[400, 300], upload_to="blog_img/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

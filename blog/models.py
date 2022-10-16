from django.db import models

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
    tags = models.ManyToManyField(Tags, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_img/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

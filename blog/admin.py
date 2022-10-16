from django.contrib import admin

from .models import Blog, Category, Tags

admin.site.register(Category),

admin.site.register(Tags)


admin.site.register(Blog)

from django.contrib import admin

from .models import Blog, Category, Tags


# admin.site.register(Category),
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["title"]


admin.site.register(Tags, TagAdmin)


class MyBlogAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "slug", "category", "created_at"]
    list_filters = ["title", "category"]
    ordering = ["created_at", "title"]
    search_fields = ["title"]


admin.site.register(Blog, MyBlogAdmin)

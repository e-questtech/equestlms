from django.contrib import admin

from .models import Blog, Category, Tags


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    ordering = ["created_at", "name"]
    search_fields = ["title"]


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["title"]


@admin.register(Blog)
class MyBlogAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "slug", "category", "created_at"]
    list_filters = ["title", "category"]
    ordering = ["created_at", "title"]
    search_fields = ["title"]

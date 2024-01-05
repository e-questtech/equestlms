from django.contrib import admin

from videos.models import Video, Category, Tags


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "url"]
    list_filters = [
        "title",
        "start_date",
        "end_date",
    ]
    ordering = ["-created_at", "-updated_at", "title"]
    search_fields = ["title"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    ordering = ["created_at", "name"]
    search_fields = ["name"]
    

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]

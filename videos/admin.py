from django.contrib import admin

from videos.models import Video


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

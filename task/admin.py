from django.contrib import admin

from task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "due_date", "status"]
    list_filter = [
        "title",
        "due_date",
    ]
    ordering = ["-created_at", "-updated_at", "title"]
    readonly_fields = ["slug", "status"]
    search_fields = ["title", "content", "course"]

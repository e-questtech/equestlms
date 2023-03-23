from django.contrib import admin

from task.models import Task, TaskSubmission


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "due_date", "status", "maximum_marks"]
    list_filter = [
        "title",
        "due_date",
    ]
    ordering = ["-created_at", "-updated_at", "title"]
    readonly_fields = ["slug", "status"]
    search_fields = ["title", "content", "course"]


@admin.register(TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    list_display = ["tasks", "mark_earned", "task_file"]
    list_filter = [
        "mark_earned",
        "task_file",
    ]
    ordering = ["-date_submitted"]

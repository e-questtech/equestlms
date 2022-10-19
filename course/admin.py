from django.contrib import admin

from course.models import ClassRoom, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "preview", "duration_as_weeks", "price", "tutors"]
    list_filter = [
        "title",
        "start_date",
        "end_date",
    ]
    ordering = ["-created_at", "-updated_at", "title"]
    readonly_fields = ["slug"]
    search_fields = ["title", "price", "overview", "tutor"]


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ["tutor", "course"]
    list_filter = ["tutor", "course"]
    ordering = [
        "-created_at",
        "-updated_at",
    ]
    search_fields = ["tutor", "course"]

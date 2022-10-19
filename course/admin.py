from django.contrib import admin

from course.models import ClassRoom, Course, CourseCategory


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "preview", "duration_as_weeks", "price", "tutor"]
    list_filter = [
        "title",
        "start_date",
        "end_date",
    ]
    ordering = ["-created_at", "-updated_at", "title"]
    readonly_fields = ["slug"]
    search_fields = ["title", "price", "overview", "tutor"]


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    list_filter = [
        "title",
    ]
    ordering = ["title"]
    search_fields = ["title"]


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ["tutor", "course"]
    list_filter = ["tutor", "course"]
    ordering = [
        "-created_at",
        "-updated_at",
    ]
    search_fields = ["tutor", "course"]

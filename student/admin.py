from django.contrib import admin

from student.models import Student


@admin.register(Student)
class TutorAdmin(admin.ModelAdmin):
    list_display = ["user", "enrolled"]
    list_filter = ["user", "created_at", "updated_at"]
    ordering = ["-created_at", "-updated_at", "user"]
    search_fields = ["user", "course"]

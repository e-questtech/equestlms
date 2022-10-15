from django.contrib import admin

from tutor.models import Tutor


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ["user", "bio"]
    list_filter = ["user", "created_at", "updated_at"]
    ordering = ["-created_at", "-updated_at", "user"]
    search_fields = ["user", "bio"]

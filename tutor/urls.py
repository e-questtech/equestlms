from django.urls import path

from tutor import views

app_name = "tutor"

urlpatterns = [
    path("", view=views.TutorListView.as_view(), name="tutor_list"),
    path("profile", view=views.TutorDashboardView.as_view(), name="tutor_dashboard"),
    path("course", view=views.TutorDashboardView.as_view(), name="tutor_course"),
    path("task", view=views.TutorDashboardView.as_view(), name="tutor_task"),
]

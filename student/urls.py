from django.urls import path

from student import views

app_name = "student"

urlpatterns = [
    path("", view=views.StudentDashBoard.as_view(), name="student_dashboard"),
    path("student-tasks", view=views.StudentTaskView.as_view(), name="student_task"),
    path("task-subit", view=views.StudentTaskSubmit.as_view(), name="task_submit"),
    path(
        "<slug:slug>",
        view=views.StudentTaskDetailView.as_view(),
        name="student_task_detail",
    ),
]

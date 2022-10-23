from django.urls import path

from course import views as course_view

app_name = "course"
urlpatterns = [
    path(
        "available-course/",
        view=course_view.AvailableCourseListView.as_view(),
        name="available-course",
    ),
    path(
        "<slug:slug>",
        view=course_view.CourseDetailView.as_view(),
        name="course-detail",
    ),
    path(
        "handle-purchase/<int:pk>/",
        view=course_view.HandlePurchaseView.as_view(),
        name="handle-purchase",
    ),
]

from django.urls import path

from videos import views

app_name = "videos"

urlpatterns = [
    path("", view=views.VideoListView.as_view(), name="video_list")
]

from django.urls import path

from videos import views

app_name = "videos"

urlpatterns = [
    path("", view=views.VideoListView.as_view(), name="video_list"),
    path("category/<str:slug>/", view=views.VideoCategoryListView.as_view(), name="video_category"),
    path("search", view=views.VideoSearchListView.as_view(), name="video_search"),
    ]


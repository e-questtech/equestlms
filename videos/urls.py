from django.urls import path

from videos import views

app_name = "videos"

urlpatterns = [
    path("", view=views.VideoListView.as_view(), name="video_list"),
    path("<int:pk>", view=views.VideoDetailView.as_view(), name="video_detail"),
    path("search/", view=views.SearchListView.as_view(), name="search_view"),
]

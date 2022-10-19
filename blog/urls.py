from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", view=views.BlogListView.as_view(), name="blog_list"),
    path("<slug:slug>", view=views.BlogDetailView.as_view(), name="blog_detail"),
    path(
        "category/<str:slug>/",
        view=views.CategoryListView.as_view(),
        name="category_detail",
    ),
    path("search/", view=views.SearchListView.as_view(), name="search_view"),
]

from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [path("", view=views.BlogListView.as_view(), name="blog_list")]

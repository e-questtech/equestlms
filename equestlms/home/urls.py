from django.urls import path

from equestlms.home import views

app_name = "home"

urlpatterns = [
    path("", view=views.IndexView.as_view(), name="index"),
    path("user/~redirect/", view=views.user_redirect_view, name="redirect"),
    path("user/~update/", view=views.user_update_view, name="update"),
    path("user/<str:username>/", view=views.user_detail_view, name="profile"),
]

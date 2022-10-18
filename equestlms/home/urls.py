from django.urls import path

from equestlms.home import views

app_name = "home"

urlpatterns = [
    path("", view=views.IndexView.as_view(), name="index"),
    path("user/~update/", view=views.ProfileUpdateView.as_view(), name="update"),
    path(
        "user/<str:username>/", view=views.ProfileUpdateView.as_view(), name="profile"
    ),
]

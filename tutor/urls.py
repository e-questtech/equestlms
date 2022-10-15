from django.urls import path

from tutor import views

app_name = "tutor"

urlpatterns = [path("", view=views.TutorListView.as_view(), name="tutor_list")]

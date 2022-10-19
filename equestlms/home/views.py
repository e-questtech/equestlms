from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from blog.models import Blog
from course.models import ClassRoom, Course, CourseCategory
from equestlms.home.forms import ProfileUpdateForm
from equestlms.home.models import CustomUser


class IndexView(ListView):

    model = Course
    template_name = "pages/home.html"
    # context_object_name = 'course'

    def get_queryset(self):
        context_object_name = Course.objects.all().order_by("-id")
        return context_object_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = Course.objects.all()
        context["classrooms"] = ClassRoom.objects.all().order_by("-id")
        context["categories"] = CourseCategory.objects.all()
        context["top_categories"] = CourseCategory.objects.filter(is_top=True).order_by(
            "-id"
        )[:7]
        context["trending"] = Course.objects.filter(is_trending=True).order_by("-id")[
            :7
        ]
        context["featured"] = Course.objects.filter(is_featured=True).order_by("-id")[
            :7
        ]
        context["blogs"] = Blog.objects.all().order_by("-id")[:10]
        return context


class UserDetailView(LoginRequiredMixin, DetailView):

    model = CustomUser
    template_name = "home/user_detail.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "users/user_detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    model = CustomUser
    form_class = ProfileUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, "Profile updated successfully")
        return reverse("home:profile", kwargs={"username": self.request.user.username})


user_detail_view = UserDetailView.as_view()


# class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

#     model = CustomUser
#     fields = ["first_name"]
#     success_message = _("Information successfully updated")

#     def get_success_url(self):
#         assert (
#             self.request.user.is_authenticated
#         )  # for mypy to know that the user is authenticated
#         return self.request.user.get_absolute_url()

#     def get_object(self):
#         return self.request.user


# user_update_view = UserUpdateView.as_view()


# class UserRedirectView(LoginRequiredMixin, RedirectView):

#     permanent = False

#     def get_redirect_url(self):
#         return reverse("users:detail", kwargs={"username": self.request.user.username})


# user_redirect_view = UserRedirectView.as_view()

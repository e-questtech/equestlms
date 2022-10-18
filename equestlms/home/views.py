from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, TemplateView, UpdateView

from equestlms.home.forms import ProfileUpdateForm
from equestlms.home.models import CustomUser


class IndexView(TemplateView):
    template_name = "pages/home.html"


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

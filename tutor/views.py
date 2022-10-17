from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View, generic

from course.models import ClassRoom, Course


class TutorListView(generic.ListView):
    model = Course
    template_name = "tutors/tutor_list.html"
    paginate_by = 5


class TutorDashboardView(View, LoginRequiredMixin):
    def get(self, request, **args):

        if self.request.user.is_staff:
            tutor = get_object_or_404(ClassRoom, tutor_id=self.request.user.id)
            context = {
                "tutor": tutor.tutor,
                "class": tutor,
            }
        else:
            messages.error(self.request, "You don't have access to this page")
            return render(
                self.request,
                "404.html",
            )
        if self.request.path == reverse("tutor:tutor_dashboard"):
            return render(self.request, "tutors/tutor_dashboard.html", context)
        if self.request.path == reverse("tutor:tutor_course"):
            return render(self.request, "tutors/tutor_courses.html", context)
        if self.request.path == reverse("tutor:tutor_task"):
            return render(self.request, "tutors/tutor_task.html", context)

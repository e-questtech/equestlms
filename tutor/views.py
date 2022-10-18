from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
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
            class_room = ClassRoom.objects.filter(tutor_id=self.request.user.id).first()
            if class_room is None:
                messages.error(
                    self.request, "You have not yet being assigned to a class"
                )
                return redirect("admin:course_classroom_add")
            tutor = ClassRoom.objects.get(tutor_id=self.request.user.id)
            context = {
                "tutor": class_room.tutor,
                "class": class_room,
                "students": class_room.student.all(),
            }
            if tutor:
                if self.request.path == reverse("tutor:tutor_dashboard"):
                    return render(self.request, "tutors/tutor_dashboard.html", context)
                if self.request.path == reverse("tutor:tutor_course"):
                    return render(self.request, "tutors/tutor_courses.html", context)
                if self.request.path == reverse("tutor:tutor_task"):
                    return render(self.request, "tutors/tutor_task.html", context)
                if self.request.path == reverse("tutor:tutor_students"):
                    return render(self.request, "tutors/tutor_students.html", context)
            else:
                if self.request.path == reverse("tutor:tutor_dashboard"):
                    return render(self.request, "tutors/tutor_dashboard.html", context)

        else:
            messages.error(self.request, "You don't have access to this page")
            return render(
                self.request,
                "404.html",
            )

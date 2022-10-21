from django.views.generic import DetailView, ListView

from course.models import Course


class AvailableCourseListView(ListView):
    model = Course
    template_name = "course/available_course.html"
    paginate_by = 25
    context_object_name = "courses"

    def get_queryset(self):
        queryset = Course.items.order_by("title")
        return queryset


class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course-details.html"
    context_object_name = "course"

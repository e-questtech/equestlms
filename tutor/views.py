from django.views import generic

from course.models import Course, StudentsInTutorCourse


class TutorListView(generic.ListView):
    model = Course
    template_name = "tutors/tutor_list.html"
    paginate_by = 5


class TutorDetailView(generic.DetailView):
    model = StudentsInTutorCourse
    template_name = "tutor/tutor_dashboard"

from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import TemplateView

from course.models import CourseCategory
from task.forms import TaskSubmissionForm
from task.models import Task


class StudentDashBoard(TemplateView):
    template_name = "student/student_dashboard.html"


class StudentTaskView(ListView):
    model = Task
    template_name = "student/student_task.html"
    context_object_name = "tasks"

    def get_queryset(self):
        context_object_name = Task.objects.all().order_by("-id")
        return context_object_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = CourseCategory.objects.all()
        context["recent"] = Task.objects.all().order_by("-id")[:4]
        return context


class StudentTaskDetailView(DetailView):
    template_name = "student/student_task_detail.html"
    model = Task
    quertset = Task.objects.all()


class StudentTaskSubmit(CreateView):
    template_name = "student/student_task_submit.html"
    form_class = TaskSubmissionForm
    model = Task
    success_url = "."

    # def form_valid(self, form):

    #    queryset = Task.objects.filter(course= self.course)
    #    form.instance.task = queryset.title

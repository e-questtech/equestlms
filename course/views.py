from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views import View
from .models import Course
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()


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


class HandlePurchaseView(View):
    """
    Sends user details to admin admin and displays purchase status to user
    """

    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.pk)
            # Email admin
            admin_email_details = {
                'subject': 'COURSE PURCHASE NOTIFICATION',
                'message': f'A user with name {user} made a  purchase request. \n User details are as follows: \n Email: {user.email}',  # type: ignore
                'recipient_list': ['solomonuche42@gmail.com'],
                'from_email': 'equestlms@equestlms.com'

            }
            send_mail(subject=admin_email_details['subject'], message=admin_email_details["message"],
                      from_email=admin_email_details['from_email'],  recipient_list=admin_email_details['recipient_list'])  # type: ignore
            # display message to user
            messages.add_message(request, messages.INFO,
                                 'Thank you for learning with Equest, your purchase request has been sent.')

        return redirect(course)

import datetime as dt
from io import BytesIO

from django.core.files.base import File
from django.test import TestCase
from django.urls import reverse
from home.models import CustomUser
from PIL import Image

from course.models import Course


class Test(TestCase):
    @staticmethod
    def get_image_file(name, ext="png", size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        """
        run this setup before any test
        """
        test_overview = """
        <p> Lorem Ipsum is simply dummy text of the printing and typesetting
        industry. Lorem Ipsum has been the industry's standard dummy text
        ever since the 1500s, when an unknown printer took a galley of type
        and scrambled it to make a type specimen book. It has survived not
        only five centuries,<b> but also the leap into electronic typesetting,
        remaining essentially unchanged. It was popularised in the 1960s with
        the release of Letraset sheets containing Lorem Ipsum passages, and
        more recently with desktop publishing software like
        Aldus PageMaker including versions of Lorem Ipsum </p>
        """
        cls.course = Course.objects.create(
            title="Hello World",
            overview=test_overview,
            price=400,
            cover_image=Test.get_image_file("test.png"),
            start_date=dt.date(2022, 1, 1),
            end_date=dt.date(2022, 1, 8),
        )
        cls.slug = Test.course.slug

        CustomUser.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="adminpassword",
            first_name="Admin",
            last_name="User",
        )

    # Models
    def test_course_is_created(self):
        """
        Test if the command creates a course
        """
        self.assertEqual(Course.objects.count(), 1)

    def test_course_duration(self):
        """
        Test if course duration is correct
        """
        course = Course.objects.get(id=1)
        self.assertEqual(course.duration_as_weeks, 1)

    def test_course_preview(self):
        """
        Test if the overview is truncated to 50 chars
        """
        course = Course.objects.get(id=1)
        self.assertLess(len(course.preview), len(course.overview))
        self.assertEqual(len(course.preview), 50)

    def test_striptags_success_in_course_preview(self):
        course = Course.objects.get(id=1)
        self.assertNotRegex(course.preview, r"<.*?>")

    # Views
    def test_view_url_exists_at_desired_location(self):
        """
        Test to check if course detail url is at desired location
        """
        response = self.client.get(f"/course/{Test.slug}")
        self.assertEqual(response.status_code, 200)

    def test_course_detail_view_url_accessible_by_name(self):
        """
        Test if course detail can be access by url name
        """
        response = self.client.get(
            reverse("course:course-detail", kwargs={"slug": Test.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_course_get_absolute_url_is_working(self):
        """
        Test to check if course.get_absolute_url works
        """
        url = Test.course.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(url, f"/course/{Test.slug}")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse("course:course-detail", kwargs={"slug": Test.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course/course_detail.html")

    def test_if_context_data_exist(self):
        response = self.client.get(
            reverse("course:course-detail", kwargs={"slug": Test.slug})
        )
        self.assertTrue("course" in response.context)

    def test_all_context_data(self):
        response = self.client.get(
            reverse("course:course-detail", kwargs={"slug": Test.slug})
        )

        self.assertEqual(
            response.context["course"].cover_image.url,
            f"/uploads/{Test.course.cover_image}",
        )

        self.assertEqual(response.context["course"].title, Test.course.title)

        self.assertEqual(response.context["course"].overview, Test.course.overview)

        self.assertEqual(response.context["course"].price, Test.course.price)

        self.assertEqual(
            response.context["course"].duration_as_weeks, Test.course.duration_as_weeks
        )

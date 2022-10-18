from django.test import TestCase
from django.urls import reverse
from .models import Video


class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Video.objects.create(
            title="How to Master Python",
            alt_image="/equestlms/static/img/bank-image.png",
            url="https://github.com/users/Victhereum/projects/4/views/1",
        )

    def test_title_label(self):
        # confirms that title field have correct label
        video = Video.objects.get(pk=1)
        title_label = video._meta.get_field("title").verbose_name
        self.assertEqual(title_label, "title")

    def test_str_method(self):
        # confirms that Video Model instance returns title
        video = Video.objects.get(pk=1)
        self.assertEqual(video.__str__(), video.title)
        return super().setUpTestData()


class VideoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        pass

    def test_view_url_exist(self):
        response = self.client.get('/videos/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('videos:video_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_name_returns_desired_url(self):
        url = reverse('videos:video_list')
        self.assertEqual(url, '/videos/')

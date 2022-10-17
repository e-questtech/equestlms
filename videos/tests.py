from django.test import TestCase

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

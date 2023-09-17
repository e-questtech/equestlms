from django.views.generic import ListView

from videos.models import Video


class VideoListView(ListView):
    model = Video
    context_object_name: str = "video_list"
    template_name: str = "videos/video_list.html"
    paginate_by = 1
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_videos"] = Video.objects.all().order_by("-created_at")[:3]
        return context

from django.db.models import Q
from django.views.generic import DetailView, ListView

from videos.models import Video


class VideoDetailView(DetailView):
    model = Video
    template_name = "videos/video_detail.html"
    paginate_by = 3
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_videos"] = Video.objects.exclude(pk=self.kwargs["pk"]).order_by(
            "-created_at"
        )[:3]
        return context


class VideoListView(ListView):

    model = Video
    context_object_name = "video_list"
    template_name = "videos/video_list.html"
    paginate_by = 3
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_videos"] = Video.objects.all().order_by("-created_at")[:3]
        return context


class SearchListView(ListView):
    model = Video
    template_name = "video/search_list.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Video.objects.filter(Q(title__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent"] = Video.objects.all().order_by("-id")[:4]
        return context

from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from videos.models import Video, Category, Tags


class VideoListView(ListView):
    model = Video
    context_object_name: str = "video_list"
    template_name: str = "videos/video_list.html"
    paginate_by = 5
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_videos"] = Video.objects.all().order_by("-created_at")[:3]
        context["categories"] = Category.objects.all().order_by("-id")[:5]
        context["tags"] = Tags.objects.all().order_by("-id")

        return context
    

class VideoCategoryListView(ListView):
    model = Video
    context_object_name: str = "video_category"
    template_name: str = "videos/video_category.html"

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return super().get_queryset().filter(category=category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_videos"] = Video.objects.all().order_by("-created_at")[:3]
        context["categories"] = Category.objects.all().order_by("-id")[:5]
        context["tags"] = Tags.objects.all().order_by("-id")
        return context

    
class VideoSearchListView(ListView):
    model = Video
    template_name: str = "videos/video_search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        search_video = Video.objects.filter(Q(title__icontains=query))
        return search_video
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_videos"] = Video.objects.all().order_by("-created_at")[:3]
        context["categories"] = Category.objects.all().order_by("-id")[:5]
        context["tags"] = Tags.objects.all().order_by("-id")
        return context


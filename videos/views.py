from django.views.generic import TemplateView
from videos.models import Video


class VideoListView(TemplateView):
    template_name: str = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_list'] = Video.objects.all()
        context['latest_videos'] = Video.objects.all().order_by('-created_at')[:3]
        return context

from django.views.generic import TemplateView

class VideoListView(TemplateView):
  template_name: str = 'videos/video_list.html'
from django.views.generic import TemplateView


class BlogListView(TemplateView):
    template_name = "blog/blog_list.html"

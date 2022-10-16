from django.views.generic import DetailView, ListView

from .models import Blog, Category, Tags

# class BlogListView(TemplateView):
#     template_name = "blog/blog_list.html"
#     paginate_by = 2


# def get_context_data(self, **kwargs):
#      context = super(BlogListView, self).get_context_data(**kwargs)
#      context['blog'] = Blog.objects.all().order_by('-id')
#      context['cats'] = Category.objects.all()
#      return context


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blog"
    paginate_by = 2

    def get_queryset(self):
        context_object_name = Blog.objects.all().order_by("-id")
        return context_object_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = Category.objects.all()
        context["tags"] = Tags.objects.all()
        context["recent"] = Blog.objects.all().order_by("-id")[:4]
        return context


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    model = Blog
    quertset = Blog.objects.all()

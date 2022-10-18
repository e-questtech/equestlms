from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Blog, Category, Tags


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
        context["category"] = Category.objects.all()
        context["tags"] = Tags.objects.all()
        context["recent"] = Blog.objects.all().order_by("-id")[:4]
        return context


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    model = Blog
    quertset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["tags"] = Tags.objects.all()
        context["recent"] = Blog.objects.all().order_by("-id")[:4]
        return context


class CategoryListView(ListView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog/category_detail.html"

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return super().get_queryset().filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["tags"] = Tags.objects.all()
        context["recent"] = Blog.objects.all().order_by("-id")[:4]
        return context


class SearchListView(ListView):
    model = Blog
    template_name = "blog/search_detail.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Blog.objects.filter(Q(title__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["tags"] = Tags.objects.all()
        # context["blog"] = Blog.objects.all()
        context["recent"] = Blog.objects.all().order_by("-id")[:4]
        return context

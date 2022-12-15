from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    latest_posts = model.objects.all().order_by("-date")[:3]
    context_object_name = "posts"
    # ordering = ["-date"]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     data = queryset[:3]
    #     return data

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"

# def posts(request):

#     all_posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })

class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tag.all()
        return context

# def post_detail(request, slug):
#     identified_post = Post.objects.get(slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post":  identified_post,
#         "post_tags": identified_post.tag.all()
#     })

         
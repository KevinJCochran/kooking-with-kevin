from django.shortcuts import render

# Create your views here.
from .models import BlogPost


def home(request):
    blog_posts = BlogPost.objects.all()
    featured_post = blog_posts[0]
    return render(request, 'blog/home.html', {
        'blog_posts': blog_posts,
        'featured_post': featured_post,
    })

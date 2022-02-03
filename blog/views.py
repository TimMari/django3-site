from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(request):
    task = Blog.objects.order_by('-id')
    return render(request, 'blog/blog.html', {'tasks':task})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'id': blog})
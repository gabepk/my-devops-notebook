""" Esse modulo define o(s) post(s) que serao mostrados nas views """

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

def render_roadmap(request):
    posts = []
    if request.user.is_authenticated:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/roadmap.html', {'posts':posts})

def post_list(request):
    """ Mostra todos os posts com data de publicacao nao vazia """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, slug):
    """ Mostra post com slug == post.slug """
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post})

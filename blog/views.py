""" Esse modulo define o(s) post(s) que serao mostrados nas views """

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    """ Mostra todos os posts com data de publicacao nao vazia """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

#def post_detail(request, pk):
#    """ Mostra post com primary key == pk """
#    post = Post.objects.get(pk=pk)
#    return render(request, 'blog/post_detail.html', {'post':post})

def post_detail(request, pk):
    """ Mostra post com primary key == pk """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
""" Esse modulo define o(s) post(s) que serao mostrados nas views """

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

def render_roadmap(request):
    return render(request, 'blog/roadmap.html', {})


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

def post_new(request):
    """ Form para adicao de novo post """
    if request.method == "POST":
        print('aqui 1')
        form = PostForm(request.POST)
        if form.is_valid():
            print('aqui 2')
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        print('aqui 3')
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form':form})
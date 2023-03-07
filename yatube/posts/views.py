from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NUM_POSTS_ON_SCREEN = 10


def index(request):
    posts = Post.objects.select_related('group').all()[:NUM_POSTS_ON_SCREEN]
    context = {'posts': posts, }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUM_POSTS_ON_SCREEN]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

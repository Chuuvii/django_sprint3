from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from .models import Post, Category


def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    ).select_related('category', 'location').order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        pk=post_id,
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now()
    ).select_related('category', 'location').order_by('-pub_date')
    return render(request, 'blog/category.html', {'category': category,
                                                  'post_list': post_list})

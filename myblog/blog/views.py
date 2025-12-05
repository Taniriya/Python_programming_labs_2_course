# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone
from django.db.models import Q
from .forms import CommentForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(published_date__lte=timezone.now())

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-published_date')

    return render(request, 'blog/post_search.html', {
        'posts': posts,
        'query': query
    })

def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    # Пагинация: 5 постов на страницу
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, показываем первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница вне диапазона, показываем последнюю страницу
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Получаем одобренные комментарии
    comments = post.comments.filter(approved_comment=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category, published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})
from django.shortcuts import render
from django.core.paginator import Paginator
from posts.models import Post

def feed_view(request):
    user = request.user

    followed_users = [f.following for f in user.following.all()]

    authors = followed_users + [user]

    posts_list = (
        Post.objects.filter(author__in=authors, is_deleted=False)
        .select_related('author')
        .prefetch_related('likes', 'comments')
        .order_by('-created_at')
    )

    paginator = paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'core/feed.html', {'posts': posts})

from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
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

    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            'posts/post_list.html',
            {'posts': posts},
            request=request
        )
        return JsonResponse({
            'html': html,
            'has_next': posts.has_next()
        })

    return render(request, 'core/feed.html', {'posts': posts})

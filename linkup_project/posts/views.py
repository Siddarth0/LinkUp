from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, PostLike, Comment
from .forms import PostForm, CommentForm

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('core:feed')
    else:
        form = PostForm()
    
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_deleted=False)
    user = request.user

    like,created = PostLike.objects.get_or_create(post=post, user=user)

    if not created:
        like.delete()
    
    return redirect(request.META.get('HTTP_REFERER', 'core:feed'))


@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_deleted=False)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(request.META.get('HTTP_REFERER', 'core:feed'))
    else:
        form = CommentForm()
    
    return render(request, 'posts/comment_form.html', {'form':form})

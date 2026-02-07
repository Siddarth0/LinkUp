from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
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


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('core:feed')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('core:feed')
    
    return render(request, 'posts/delete_post.html', {'post': post})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('core:feed')
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'posts/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    
    if request.method == 'POST':
        comment.delete()
        return redirect('core:feed')
    
    return render(request, 'posts/delete_comment.html', {'comment': comment})

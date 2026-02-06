from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from accounts.models import User
from .models import Follow

@login_required
def toggle_follow(request, user_id):
    current_user = request.user
    target_user = get_object_or_404(User, id=user_id)

    if current_user == target_user:
        messages.error(request, "You cannot follow yourself.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    follow = Follow.objects.filter(follower=current_user, following=target_user).first()
    if follow:
        follow.delete()
        messages.success(request, f"You have unfollowed {target_user.username}.")
    else:
        Follow.objects.create(follower=current_user, following=target_user)
        messages.success(request, f"You are now following {target_user.username}.")

    return redirect(request.META.get('HTTP_REFERER', '/'))

from django import template

register = template.Library()

@register.filter
def is_liked_by(post, user):
    if not user.is_authenticated:
        return False
    return post.likes.filter(user=user).exists()

@register.filter
def is_following(target_user, current_user):
    if not current_user.is_authenticated:
        return False
    return target_user.followers.filter(follower=current_user).exists()

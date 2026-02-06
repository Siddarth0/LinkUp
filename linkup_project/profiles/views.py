from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import User
from posts.models import Post
from .forms import ProfileForm

def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    posts = Post.objects.filter(author=user).order_by('-created_at')
    
    context = {
        'profile_user': user,
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'profiles/profile_detail.html', context)


def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_detail',username = request.user.username)
        else:
            form = ProfileForm(instance=profile)
    
    return render(request, 'profiles/profile_edit.html', {'form':form})

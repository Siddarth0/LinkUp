from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notification_view(request):
    notifications = Notification.objects.filter(receiver=request.user).select_related('sender','post')

    notifications.filter(is_read=False).update(is_read=True)
    
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

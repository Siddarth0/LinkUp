from django.urls import path
from . import views

app_name = 'follows'

urlpatterns = [
    path('<int:user_id>/toggle/', views.toggle_follow, name='toggle_follow'),
]

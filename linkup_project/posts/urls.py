from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/',views.create_post, name = 'create_post'),
    path('<int:post_id>/like/', views.like_post, name='like_post'),
    path('<int:post_id>/comment/', views.comment_post, name='comment_post'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('<int:post_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('<int:post_id>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
]

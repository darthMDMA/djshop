from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_home, name='blog'),
    path('posts/', PostsListView.as_view(), name='all_posts_url'),
    path('posts/<str:username>/', UserPostListView.as_view(), name='user_posts_url'),
    path('posts/<str:username>/<slug:post_slug>-<int:post_id>/', PostDetail.as_view(), name='post_url'),
    path('add_post/', AddPost.as_view(), name='add_post_url'),
    path('posts/<str:username>/<slug:post_slug>-<int:post_id>/edit_post', EditPost.as_view(), name='edit_post_url'),
    path('posts/<str:username>/<slug:post_slug>-<int:post_id>/delete_post', DeletePost.as_view(), name='delete_post_url'),
    path('tags/', TagsList.as_view(), name='all_tags_url'),
    path('tags/<slug:tag_slug>/', show_tag, name='tag_url'),

]

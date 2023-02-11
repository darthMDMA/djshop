from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('blog/', blog_home, name='blog'),
    path('blog/posts/', PostsListView.as_view(), name='all_posts'),
    path('blog/posts/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('blog/posts/<str:username>/<slug:post_slug>-<int:post_id>/', show_post, name='post'),
    path('blog/add_post/', AddPost.as_view(), name='add_post'),
]

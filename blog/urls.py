from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', blog_home, name='blog'),
    path('posts/', PostsListView.as_view(), name='all_posts_url'),
    path('posts/<str:username>/', UserPostListView.as_view(), name='user_posts_url'),
    path('posts/<str:username>/<slug:post_slug>-<int:post_id>/', PostDetail.as_view(), name='post_url'),
    path('add_post/', AddPost.as_view(), name='add_post_url'),
    path('posts/edit_post/<str:username>/<slug:post_slug>-<int:post_id>/', editpost, name='edit_post_url'),
    path('tags/', TagsList.as_view(), name='all_tags_url'),
    path('tags/<slug:tag_slug>/', show_tag, name='tag_url'),

]

from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('discussions/',  discussions_home, name='discussions'),
    path('discussions/create/',  discussion_create, name='discussion_create'),
    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'), #дописать
]
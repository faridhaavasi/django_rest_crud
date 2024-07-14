from django.urls import path
from apps.blog.v1.views.post_views import PostsShow

app_name = 'blog'

urlpatterns = [
    path('show_posts/', PostsShow.as_view(), name='show_posts'),
]

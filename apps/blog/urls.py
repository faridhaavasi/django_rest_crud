from django.urls import path
from apps.blog.v1.views.post_views import PostsShowDetail, CreatPost

app_name = 'blog'

urlpatterns = [
    path('show_posts/', PostsShowDetail.as_view(), name='show_posts'),
    path('detail_posts/<int:pk>', PostsShowDetail.as_view(), name='detail_posts'),
    path('create_post', CreatPost.as_view(), name='create_post')
]

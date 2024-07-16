from django.urls import path
from apps.blog.v1.views.post_views import PostsShowDetail, CreatPost, UpdatePost, DeletePost

app_name = 'blog'

urlpatterns = [
    path('show_posts/', PostsShowDetail.as_view(), name='show_posts'),
    path('detail_posts/<int:pk>', PostsShowDetail.as_view(), name='detail_posts'),
    path('create_post', CreatPost.as_view(), name='create_post'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePost.as_view(), name='delete_post'),
]

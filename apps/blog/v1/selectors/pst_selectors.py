from django.db.models import QuerySet
from apps.blog.models import Post


def select_post_all() -> QuerySet:
    return Post.objects.all()


def select_post_specific_instance(pk: int) -> Post:
    return Post.objects.get(pk=pk)


def delete_post(pk:int) -> Post:
    post = Post.objects.get(pk=pk)
    if post:
        return post.delete()
    return 'post dos not exists'
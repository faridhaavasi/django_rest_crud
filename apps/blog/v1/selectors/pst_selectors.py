from django.db.models import QuerySet
from apps.blog.models import Post


def select_post_all() -> QuerySet:
    return Post.objects.all()


def select_post_specific_instance(pk:int) -> QuerySet:
    return Post.objects.get(pk=pk)
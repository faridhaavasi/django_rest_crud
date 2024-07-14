from apps.blog.models import Post

def post_create_instance(user_id: int, title: str, description: str) -> Post:
    return Post.objects.create(
        author_id=user_id,
        title=title,
        description=description
    )

def post_update_instance(pk: int, **kwargs) -> Post:
    instance = Post.objects.get(pk=pk)
    for attr, value in kwargs.items():
        setattr(instance, attr, value)
    instance.save()
    return instance
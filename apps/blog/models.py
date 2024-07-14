from django.db import models
from apps.common.models import BaseModel

from django.contrib.auth.models import User


from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}-{self.author.username}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

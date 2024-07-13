from django.db import models
from apps.common.models import BaseModel

from django.contrib.auth.models import User


class Post(BaseModel):
    auther = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts',
                               db_index=True)
    tite = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.tite}-{self.auther.username}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

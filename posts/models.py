from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    title = models.TextField()
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return f'title:{self.title}, author: {self.author}'

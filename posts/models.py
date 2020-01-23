from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify


class Post(models.Model):
    title = models.TextField()
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now)
    slug_title = models.SlugField(max_length=60, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'title:{self.title}, author: {self.author}'


class HashTag(models.Model):
    hash_tag = models.CharField(max_length=45, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return f'Hashtag:{self.hash_tag}'

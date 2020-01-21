from django.db import models
from django.contrib.auth.models import User


class HashTag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'gallery/user_{instance.user.id}/{filename}'


class Gallery(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    about = models.CharField(max_length=300, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hashtag = models.ManyToManyField(HashTag, null=True, blank=True)

from pathlib import Path
from django.contrib.auth.models import User
from django.db import models
from ma_book.settings import MAX_STATUS_LENGTH
from ma_book.settings import MEDIA_ROOT, MEDIA_URL


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.user.username}.{ext}"
    return Path("avatars", filename)


class UserProfile(models.Model):
    birthday = models.DateField("Birthday")
    avatar = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    status = models.CharField(max_length=MAX_STATUS_LENGTH, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'UserName:{self.user}'


class Relations(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, related_name="current_user")
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by_current_user")
    started = models.DateTimeField(auto_now_add=True, db_index=True)

    def __repr__(self):
        return f"{self.current_user} follows {self.follows}"

from pathlib import Path
from django.contrib.auth.models import User
from django.db import models
from ma_book.settings import MAX_STATUS_LENGTH
from ma_book.settings import MEDIA_ROOT, MEDIA_URL


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.user.username}.{ext}"
    return Path(MEDIA_ROOT, "avatars", filename)


class UserProfile(models.Model):
    birthday = models.DateField("Birthday")
    avatar = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    status = models.CharField(max_length=MAX_STATUS_LENGTH, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

from django.contrib.auth.models import User
from django.db import models
from ma_book.settings import MAX_STATUS_LENGTH


class UserProfile(models.Model):
    birthday = models.DateField("Birthday")
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    status = models.CharField(max_length=MAX_STATUS_LENGTH, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)


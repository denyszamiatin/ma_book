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


# class Follower(models.Model):
#     user_from = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     user_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, db_index=True)
#
#     class Meta:
#         unique_together = ('follower', 'following')
#
#     def __str__(self):
#         return "{} follows {}".format(self.user_from, self.user_to)
#
#
# UserProfile.add_to_class('following', models.ManyToManyField(
#     'self', through=Follower, related_name='followers', symmetrical=False
# ))

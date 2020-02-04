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
        return f'Username:{self.user}'


class Relations(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, related_name="current_user")
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by_current_user")
    started = models.DateTimeField(auto_now_add=True, db_index=True)

    def __repr__(self):
        return f"{self.current_user} follows {self.follows}"

    @classmethod
    def get_followers(cls, username, number=-1):
        """
        Return list of followers of a user. If parameter number is not set or negative, return all followers.
        :param username: str  --  username of a user who's follower to return
        :param number: int  --  number of followers to return
        :return: list
        """
        if not isinstance(number, int):
            raise TypeError('Integer value expected')
        user = User.objects.get(username=username)
        if number > 0:
            followers = [relation.current_user for relation in cls.objects.filter(follows=user)][:number]
        else:
            followers = [relation.current_user for relation in cls.objects.filter(follows=user)]
        return followers

    @classmethod
    def get_who_i_follow(cls, username, number=-1):
        """
        Return list of all people who user follows
        :param username: str  --  username of user who follows
        :param number: int  -- number of people who user follows to return
        :return: list
        """
        if not isinstance(number, int):
            raise TypeError('Integer value expected')
        user = User.objects.get(username=username)
        if number > 0:
            people_i_follow = [relation.follows for relation in cls.objects.filter(current_user=user)][:number]
        else:
            people_i_follow = [relation.follows for relation in cls.objects.filter(current_user=user)]
        return people_i_follow

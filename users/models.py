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


class FollowersManager(models.Manager):
    def get_followers(self, username, number=-1):
        """
        Return list of followers of a user. If parameter 'number' is not set or is not positive, return all followers.
        :param username: str  --  username of a user who's follower to return
        :param number: int  --  number of followers to return
        :return: list
        """
        if not isinstance(number, int):
            raise TypeError('Integer value expected')
        from django.db import connection
        user_id = User.objects.get(username=username).id
        query = f"SELECT current_user_id FROM users_relations WHERE follows_id = {user_id}"
        if number > 0:
            query = query + f"LIMIT {number}"
        with connection.cursor() as cursor:
            cursor.execute(query)
            followers = [User.objects.get(id=id_[0]) for id_ in cursor.fetchall()]
        return followers

    def get_who_i_follow(self, username, number=-1):
        """
        Return list of all people who user follows
        :param username: str  --  username of user who follows
        :param number: int  -- number of people who user follows to return
        :return: list
        """
        if not isinstance(number, int):
            raise TypeError('Integer value expected')
        from django.db import connection
        user_id = User.objects.get(username=username).id
        query = f"SELECT follows_id FROM users_relations WHERE current_user_id = {user_id}"
        if number > 0:
            query = query + f"LIMIT {number}"
        with connection.cursor() as cursor:
            cursor.execute(query)
            people_i_follow = [User.objects.get(id=id_[0]) for id_ in cursor.fetchall()]
        return people_i_follow

    def get_friends_list(self, username):
        """
        Return the friends list
        (people who follows you and you follow them)
        :return:
        """
        followed = self.get_who_i_follow(username=username)
        followers = self.get_followers(username=username)
        friends_list = [i for i in followed if i in followers]
        friends_objects = User.objects.filter(username__in=friends_list)
        return friends_objects


class Relations(models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, related_name="current_user")
    follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by_current_user")
    started = models.DateTimeField(auto_now_add=True, db_index=True)

    objects = FollowersManager()

    def __repr__(self):
        return f"{self.current_user} follows {self.follows}"

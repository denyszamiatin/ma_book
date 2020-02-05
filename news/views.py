from django.shortcuts import render
from posts.models import Post
from users.models import FollowersManager
# Create your views here.


def news_view(request):
    followers = FollowersManager()
    who_i_follow = followers.get_who_i_follow(username=request.user)
    news_objects = Post.objects.all().filter(author__in=who_i_follow).order_by('-created_date')
    context = {
        'news_objects': news_objects
    }
    return render(request, 'news.html', context)

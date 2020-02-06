from django.shortcuts import render
from posts.models import Post
from users.models import Relations
# Create your views here.


def news_view(request):
    who_i_follow = Relations.objects.get_who_i_follow(username=request.user)
    news_objects = Post.objects.all().filter(author__in=who_i_follow).order_by('-created_date')
    context = {
        'news_objects': news_objects
    }
    return render(request, 'news.html', context)


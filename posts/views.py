from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], text=form.cleaned_data['text'], author=request.user)
            post.save()
            return redirect('posts:create_post')
    return render(request, 'create_post.html', {'form': form})

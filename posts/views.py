from django.shortcuts import render, redirect
from .forms import PostForm


def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:create_post')
    return render(request, 'create_post.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db import IntegrityError
from .forms import PostForm, EditPostForm, HashTagForm
from .models import Post, HashTag
from .utils import hash_tag_validation


def create(request):
    form = PostForm()
    hash_tag_form = HashTagForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        hash_tag_form = HashTagForm(request.POST)
        if form.is_valid() and hash_tag_form.is_valid():
            post = Post(title=form.cleaned_data['title'], text=form.cleaned_data['text'], author=request.user)
            post.save()
            hash_tags = hash_tag_form.cleaned_data['hash_tags'].split()
            for hash_tag in hash_tags:
                if hash_tag_validation(hash_tag):
                    try:
                        tag = HashTag(hash_tag=hash_tag)
                        tag.save()
                        tag.posts.add(post)
                    except IntegrityError:
                        tag = HashTag.objects.filter(hash_tag=hash_tag).first()
                        tag.posts.add(post)
            return redirect(reverse('posts:show'))
    return render(request, 'create.html', {'form': form, 'hash_tag_form': hash_tag_form})


def edit(request):
    post = get_object_or_404(Post, slug_title=request.GET['slug_title'])
    form = EditPostForm(instance=post)
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        form.save()
        return redirect(reverse('posts:show'))
    return render(request, 'edit.html', {'form': form})


def show(request):
    post = Post.objects.filter(author=request.user.id)
    return render(request, 'posts_list.html', {'posts': post})

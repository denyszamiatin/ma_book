from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, UserProfile, Relations
from .forms import RegistrationForm, UserProfileForm, LoginForm, SearchForm, EditUserForm, EditUserProfileForm, EditUserAvatar


def user_registration(request):
    user_form = RegistrationForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Successful registration')
            return redirect(reverse('users:login'))
    return render(request, 'users/registration.html', {
        "user_form": user_form,
        "profile_form": profile_form,
    })


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = authenticate(request, username=username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "Congratulations! Now you logged in.")
                return redirect(f"/user/profile/{username}")
            else:
                messages.error(request, "Invalid username or password!")
        else:
            messages.error(request, "Invalid input!")
    return render(request, 'users/login.html', {
        'form': form,
        'title': 'Login page'
    })


@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)
    my_followers = [relation.current_user for relation in Relations.objects.filter(follows=user)]
    i_follow = [relation.follows for relation in Relations.objects.filter(current_user=user)]
    context = {
        'username': username,
        'my_followers': my_followers,
        'i_follow': i_follow
    }
    return render(request, 'users/profile.html', context)


@login_required
def search(request):
    form = SearchForm()
    search_result = []
    user_follows = [relation.follows for relation in Relations.objects.filter(current_user=request.user)]
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            fields = [(name, value) for name, value in form.cleaned_data.items() if value]
            search_result = User.objects
            for field in fields:
                if field[0] == 'birthday':
                    filter_by = f'userprofile__{field[0]}__startswith'
                else:
                    filter_by = f'{field[0]}__startswith'
                search_result = search_result.filter(**{filter_by: field[1]})

    context = {'form': form, 'search_result': search_result.all(), 'user_follows': user_follows}
    return render(request, 'users/search.html', context)


def edit_user_profile(request):
    user_form = EditUserForm(instance=request.user)
    profile = UserProfile.objects.get(user=request.user)
    profile_form = EditUserProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditUserProfileForm(request.POST, instance=profile)
        avatar_form = EditUserAvatar(request.POST, request.FILES, instance=profile)
        if avatar_form.is_valid() and user_form.is_valid() and profile_form.is_valid():
            avatar_form.user = request.user
            profile_form.user = request.user
            avatar_form.save()
            user_form.save()
            profile_form.save()
            return redirect(reverse('users:profile'))
        elif user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.user = request.user
            profile_form.save()
            return redirect(reverse('users:profile'))
    return render(request, 'users/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'img': profile.avatar.url,
    })


@login_required
def follow(request, username):
    new_relation = Relations(current_user=request.user, follows=User.objects.get(username=username))
    new_relation.save()
    return redirect(reverse('users:search'))

@login_required
def unfollow(request, username):
    old_relation = Relations.objects.get(current_user=request.user, follows=User.objects.get(username=username))
    old_relation.delete()
    return redirect(reverse('users:search'))

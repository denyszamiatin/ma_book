from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm, UserProfileForm, LoginForm
from django.contrib import messages


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
            return redirect('/')
    return render(request, 'users/registration.html', {
        "user_form": user_form,
        "profile_form": profile_form,
    })


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "Congratulations! Now you logged in.")
                return redirect(reverse('user_profile'))
            else:
                messages.error(request, "Invalid username or password!")
        else:
            messages.error(request, "Invalid input!")
    return render(request, 'users/login.html', {
        'form': form,
        'title': 'Login page'
    })


def user_profile(request):
    return render(request, 'users/profile.html')
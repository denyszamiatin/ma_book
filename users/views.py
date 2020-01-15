from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserProfileForm


def user_registration(request):
    user_form = RegistrationForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = UserProfileForm(request.POST)
            profile.save()

            return redirect('/')

    return render(request, 'users/registration.html', {
        "user_form": user_form,
        "profile_form": profile_form,
    })

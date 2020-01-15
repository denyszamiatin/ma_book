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
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password1'],
                                email=user_form.cleaned_data['email'],
                                first_name=user_form.cleaned_data['first_name'],
                                last_name=user_form.cleaned_data['last_name'],)
            profile = UserProfileForm(request.POST)
            profile.save()

            return redirect('/')

    return render(request, 'users/registration.html', {
        "user_form": user_form,
        "profile_form": profile_form,
    })

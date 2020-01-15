from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def user_registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                email=form.cleaned_data['email'],
                                first_name=form.cleaned_data['first_name'],
                                last_name=form.cleaned_data['last_name'],)
            login(request, user)
            return redirect('home')

    return render(request, 'users/registration.html', {
        "form": form
    })

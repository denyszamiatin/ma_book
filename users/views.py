from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegistrationForm, UserProfileForm, LoginForm, SearchForm
from django.contrib import messages
from .models import User


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
            return redirect(reverse('users:profile'))
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
                return redirect('users:profile')
            else:
                messages.error(request, "Invalid username or password!")
        else:
            messages.error(request, "Invalid input!")
    return render(request, 'users/login.html', {
        'form': form,
        'title': 'Login page'
    })


def user_profile(request, username):
    return render(request, 'users/profile.html', {"username": username})


def search(request):
    form = SearchForm()
    options = ('username', 'email', 'name')
    option = ''
    search_result = []
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if 'query' in request.GET:
            query = request.GET['query']
            option = request.GET['option']
            if option == 'username':
                searched = User.objects.filter(username__startswith=query).values('username')
                search_result = [username['username'] for username in searched]
            elif option == 'email':
                searched = User.objects.filter(email__startswith=query).values('username')
                search_result = [username['username'] for username in searched]
            elif option == 'name':
                searched = User.objects.values('first_name', 'last_name', 'username')
                search_result = [user['username'] for user in searched if
                          (user['first_name'].lower() + " " + user['last_name'].lower()).startswith(query.lower())]

    return render(request, 'users/search.html', {'form': form, 'search_result': search_result, 'option': option, "options": options})

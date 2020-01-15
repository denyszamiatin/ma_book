from django.shortcuts import render


def user_registration(request):
    return render(request, 'users/registration.html')

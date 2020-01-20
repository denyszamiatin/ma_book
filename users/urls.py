from django.urls import path
from .views import user_registration, user_login, user_profile


app_name = "users"

urlpatterns = [
    path('registration', user_registration, name='registration'),
    path('login', user_login, name='login'),
    path('profile', user_profile, name='profile')
]
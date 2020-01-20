from django.urls import path
from .views import user_registration, user_login, user_profile, search


app_name = "users"

urlpatterns = [
    path('registration', user_registration, name='registration'),
    path('login', user_login, name='login'),
    path('profile/<str:username>', user_profile, name='profile'),
    path('search', search, name='search'),
]

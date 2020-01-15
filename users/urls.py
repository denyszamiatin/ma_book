from django.urls import path
from .views import user_registration


app_name = "users"

urlpatterns = [
    path('registration', user_registration, name='registration'),
]
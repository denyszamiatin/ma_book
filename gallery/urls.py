from django.urls import path
from .views import add, success, get_images


app_name = "gallery"

urlpatterns = [
    path('add', add, name='add'),
    path('success', success, name='success'),
    path('images', get_images, name='images'),
]

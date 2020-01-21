from django.urls import path
from .views import add, success


app_name = "gallery"

urlpatterns = [
    path('add', add, name='add'),
    path('success', success, name = 'success'),
]
from django.urls import path
from .views import create, edit, show

app_name = "posts"

urlpatterns = [
    path('create', create, name='create'),
    path('edit', edit, name='edit'),
    path('show', show, name='show')
]

from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit'),
    path('show', views.show, name='show')
]

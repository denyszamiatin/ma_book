from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('create_post', views.create_post, name='create_post'),
    path('edit_post', views.edit_post, name='edit_post'),
    path('show_post', views.show_post, name='show_post')
]

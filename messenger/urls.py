from django.urls import path

from .views import send

app_name = "messenger"

urlpatterns = [
    path('send', send, name='send_message'),
]

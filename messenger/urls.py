from django.urls import path

from . import views

app_name = "messenger"

urlpatterns = [
    path('send', views.send, name='send_message'),
    path('', views.dialogs, name='dialogs'),
    path('dialogue/<username>', views.dialogue, name='dialogue'),
]

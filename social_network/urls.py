from django.urls import path
from .views import get_index_page


app_name = "social_network"

urlpatterns = [
    path('', get_index_page, name='index'),
]

from django.urls import path
from .views import news_view

app_name = "news"

urlpatterns = [
    path('news_view', news_view, name='news')
]

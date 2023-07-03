from django.urls import path
from .views import url_shortener, redirect_to_original_url

urlpatterns = [
    # path('', home, name='home'),
    path('', url_shortener, name='url_shortener'),
    path('<slug:short_url>/', redirect_to_original_url, name='redirect_to_original_url'),
]


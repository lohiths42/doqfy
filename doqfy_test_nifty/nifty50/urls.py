from nifty50.views import display_data
from django.urls import path

urlpatterns = [
    path('', display_data, name='display_data'),
]
from django.urls import path
from snippets.views import create_snippet, snippet_detail

urlpatterns = [
    path('create/', create_snippet, name='create_snippet'),
    path('<str:shareable_url>/', snippet_detail, name='snippet_detail'),
]

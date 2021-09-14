from django.urls import path
from .views import search, search_data

article_patterns = ([
    path('', search),
    path('result/', search_data, name='result'),
],'articles') 
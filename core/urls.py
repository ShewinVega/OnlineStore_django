from django.urls import path
from .views import home

core_patterns = ([
    path('',home,name='home')
],'cores')
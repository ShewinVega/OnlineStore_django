from os import name
from django.urls import path
from .views import home, contact

core_patterns = ([
    path('',contact,name='contact'),
    #path('contact/',contact, name='contact'),
],'cores')
from django.urls import path
from . import views

urlpatterns=[

    path('poss/',views.read,name='poss'),
    path('create/',views.create,name='create'),
    path('new/',views.new)
]
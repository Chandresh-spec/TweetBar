
from django.urls import path
from .import views

urlpatterns = [
    path('helo/',views.helo,name='helo')
]

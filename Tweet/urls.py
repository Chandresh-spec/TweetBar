
from django.urls import path
from .import views

urlpatterns = [
    path('helo/',views.helo,name='helo'),
    path('homepage/',views.homepage,name='homepage'),
    path('add_tweet/',views.addTweet_views,name='add_tweet'),
    path('edit_tweet/<int:pk>/',views.edit_tweet,name='edit_tweet'),
    path('tweet_delete/<int:pk>/',views.tweet_delete,name='tweet_delete')
]

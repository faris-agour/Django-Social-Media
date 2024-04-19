from django.urls import path

from .views import post_create, feeds, friends, search_for_friends, post_like, post_like_dash
from . import views

app_name = "post"

urlpatterns = [
    path('', feeds, name='feeds'),
    path('like/<int:pk>', post_like, name='post_like'),
    path('likes/<int:pk>', post_like_dash, name='post_like_dash'),
    path('create/', post_create, name='create'),
    path('friends/', friends, name='friends'),
    path('search_for_friends/', search_for_friends, name='search_for_friends'),
    path('send_friend_request/<int:to_user_id>/', views.add_friend, name='add_friend'),
    path('accept_friend_request/<int:friendship_id>/', views.accept_friend, name='accept_friend'),

]

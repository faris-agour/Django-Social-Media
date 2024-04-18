from django.urls import path

from .views import post_create, feeds, friends, search_for_friends
from . import views

app_name = "post"

urlpatterns = [
    path('', feeds, name='feeds'),
    path('create/', post_create, name='create'),
    path('friends/', friends, name='friends'),
    path('search_for_friends/', search_for_friends, name='search_for_friends'),
    path('send_friend_request/<int:to_user_id>/', views.add_friend, name='add_friend'),
    path('accept_friend_request/<int:friendship_id>/', views.accept_friend, name='accept_friend'),

]

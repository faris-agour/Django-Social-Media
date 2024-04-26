from django.urls import path

from .views import (PostApiView,PostDetailsApiView,PostAddApiView,
                    PostEditApiView,RegisterAPIView,loginAPIView,UserInfo,logoutAPIView)

app_name = "api"

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', loginAPIView.as_view(), name='loginAPIView'),
    path('logout/', logoutAPIView.as_view(), name='logoutAPIView'),
    path('user_info/', UserInfo.as_view(), name='UserInfo'),

    path('posts/', PostApiView.as_view(), name='PostApiView'),
    path('posts/add/', PostAddApiView.as_view(), name='PostAddApiView'),
    path('posts/<int:id>', PostDetailsApiView.as_view(), name='PostDetailsApiView'),
    path('posts/edit/<int:id>', PostEditApiView.as_view(), name='PostEditApiView'),

]

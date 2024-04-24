from django.urls import path

from .views import PostApiView,PostDetailsApiView,PostAddApiView,PostEditApiView

app_name = "api"

urlpatterns = [
    path('posts/', PostApiView.as_view(), name='PostApiView'),
    path('posts/add/', PostAddApiView.as_view(), name='PostAddApiView'),
    path('posts/<int:id>', PostDetailsApiView.as_view(), name='PostDetailsApiView'),
    path('posts/edit/<int:id>', PostEditApiView.as_view(), name='PostEditApiView'),

]

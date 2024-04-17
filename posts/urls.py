from django.urls import path

from .views import post_create, feeds

app_name = "post"

urlpatterns = [
    path('', feeds, name='feeds'),
    path('create/', post_create, name='create'),

]

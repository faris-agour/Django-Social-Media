from django.urls import path

from . import views
from .views import custom_logout_view, CustomPasswordChangeView, CustomPasswordChangeDoneView

app_name = "account"
urlpatterns = [
    # path('login/', views.user_login, name='login')
    path('login/', views.user_login, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('password-change/',
         CustomPasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard, name='dashboard'),
]

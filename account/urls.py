from django.contrib.auth import views as auth_views
# from django.urls import path, include
#
# from . import views
# from .views import custom_logout_view, CustomPasswordChangeView, CustomPasswordChangeDoneView
from .views import custom_logout_view
# app_name = "account"
# urlpatterns = [
#     path('', include('django.contrib.auth.urls')),
#     path('', views.dashboard, name='dashboard'),
#     path('register/', views.register, name='register'),
#     path('edit/', views.edit, name='edit'),
#     path('', views.dashboard, name='dashboard'),
# ]
# -----------------------------------------------------------------------------------------------------------
from django.urls import path, include

from . import views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),

    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),

    # change password urls
    # path('password-change/',
    #      auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password-change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),

    # reset password urls
    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('password-reset/complete/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),

    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    # path('register/', views.register, name='register'),
    # path('edit/', views.edit, name='edit'),
]

# from django.urls import path, include
#
# from . import views
# from .views import custom_logout_view, CustomPasswordChangeView, CustomPasswordChangeDoneView
# app_name = "account"
# urlpatterns = [
#     path('', include('django.contrib.auth.urls')),
#     path('', views.dashboard, name='dashboard'),
#     path('register/', views.register, name='register'),
#     path('edit/', views.edit, name='edit'),
#     path('', views.dashboard, name='dashboard'),
# ]
# -----------------------------------------------------------------------------------------------------------
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .views import custom_logout_view

urlpatterns = [
    path('logout/', custom_logout_view, name='logout'),

    path("change-password/",
         auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"),
         name='password_change'),

    path('', include('django.contrib.auth.urls')),
    path('profile/<int:user_id>', views.dashboard, name='dashboard'),
    path('profile/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name="signup"),
    path('edit/', views.edit, name='edit'),

]

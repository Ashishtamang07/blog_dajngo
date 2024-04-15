# from django.contrib import admin
from django.urls import path
from . import views as user_views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('',user_views.register, name='users-register' ),
    # # path('about/',views.about, name='blog-about'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login" ),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout" ),
]

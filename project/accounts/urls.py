from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),

    #path('login/', views.login_view , name='login'),

    # path('logout/', views.logout_user, name='logout'),


    path('', views.home, name='home'),

]

from django.urls import path
from . import views

#define the routers of the application
urlpatterns = [
    path('', views.homePage, name="home"),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout',views.signout, name="logout")
               ]

from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register),
    path('login/', views.loginpage,name="login"),
    path('home/', views.home,name="home"),
    path('logout/',views.logoutpage,name="logout")
]

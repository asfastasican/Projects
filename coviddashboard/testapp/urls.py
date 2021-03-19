from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/search', views.search, name='search'),
]

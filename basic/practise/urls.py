from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('cquiz', views.cquiz, name='cquiz'),
    path('cpp', views.cpp, name='cpp'),
    path('java', views.java, name='java'),
    path('python', views.python, name='python'),
    path('webdev', views.webdev, name='webdev'),
    path('search/', views.search, name='search'),
    path('otherprofile/<str:name>', views.otherprofile, name='otherprofile'),
    path('sendft/<str:myid>', views.sendfr, name='sendfr'),
    path('acceptreq/<str:myid>', views.acceptreq, name='acceptreq'),
    path('cancelreq/<str:myid>', views.cancelreq, name='cancelreq'),
    path('rmvfrnd/<str:myid>', views.rmvfrnd, name='rmvfrnd'),
]

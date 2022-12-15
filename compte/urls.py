
#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('inscrire', views.inscrire, name='inscrire'),
    path('login', views.connexion, name='login'),
    path('logout', views.deconnect, name='logout'),


 ]
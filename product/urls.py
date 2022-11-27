from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('produit', views.produit, name='produit'),
    path('<int:myid>', views.detail, name='detail'),
    path('cereal', views.cereal, name='cereal'),
    path('maraichere', views.maraichere, name='maraichere'),
    path('coton', views.coton, name='coton'),
    path('formulaire_agri', views.formulaire_agri, name='formulaire_agri'),
    path('checkout', views.checkout, name='checkout'),
    path('confirmation', views.confirmation, name='confirmation'),


]

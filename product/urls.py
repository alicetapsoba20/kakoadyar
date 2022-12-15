from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('produit', views.produit, name='produit'),
    path('product/<str:slug>/',views.detail, name="product"),
    path('cart', views.cart, name='cart'),
    path('cart/delete', views.delete_cart, name='delete-cart'),
    path('product/<str:slug>/add-to-cart/',views.add_to_cart, name="add-to-cart"),
    path('checkout', views.checkout, name='checkout'),
    path('confirmation', views.confirmation, name='confirmation'),

]

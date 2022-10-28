
from django.shortcuts import render
from urllib import request
from product.models import Produit,Agriculteur




def index(request):
    products = Produit.objects.all()
    context = {"products": products}
    
    return render(request, 'product/index.html', context)

def about(request):
    return render(request, 'product/about.html')

def agriculteur(request):

    products = Agriculteur.objects.all()
    context = {"products": products}

    return render(request, 'product/agriculteur.html', context)

def cereal(request):

    products = Produit.objects.all()
    context = {"products": products}

    return render(request, 'product/cereal.html', context)

def maraichere(request):
    return render(request, 'product/maraichere.html')

def coton(request):
    return render(request, 'product/coton.html')

def formulaire_agri(request):
    return render(request, 'product/formulaire_agri.html')

# Create your views here.


from django.shortcuts import render
from urllib import request
from .models import Product,Commande
from django.core.paginator import Paginator





def index(request):
    products = Product.objects.all()
    context = {"products": products}
    
    return render(request, 'product/index.html', context)

def about(request):
    return render(request, 'product/about.html')

# def agriculteur(request):

#     products = Agriculteur.objects.all()
#     context = {"products": products}

#     return render(request, 'product/agriculteur.html', context)

def produit(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(nom__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    # products = Agriculteur.objects.all()
    # context = {"products": products}

    # return render(request, 'product/agriculteur.html', context)
    return render(request, 'product/produit.html',{'product_object': product_object})

# def detail(request):
#     return render(request, 'product/detail.html')

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'product/detail.html', {'product': product_object})

def checkout(request):
    if request.method =="POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        comman= Commande(nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode, items=items, total=total )
        comman.save()
        return redirect ('confirmation')

    return render(request, 'product/checkout.html')

def confirmation(request):
    return render(request, 'product/confirmation.html')

def cereal(request):

    products = Product.objects.all()
    context = {"products": products}

    return render(request, 'product/cereal.html', context)

def maraichere(request):
    return render(request, 'product/maraichere.html')

def coton(request):
    return render(request, 'product/coton.html')

def formulaire_agri(request):
    return render(request, 'product/formulaire_agri.html')

# Create your views here.

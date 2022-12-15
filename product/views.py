from django.shortcuts import render, redirect, get_object_or_404
from urllib import request
from django.urls import reverse
from .models import Product,Commande,Cart,Order
from django.core.paginator import Paginator





def index(request):
    products = Product.objects.all()
    context = {"products": products}
    
    return render(request, 'product/index.html', context)

def about(request):
    return render(request, 'product/about.html')

def produit(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(nom__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'product/produit.html',{'product_object': product_object})


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/detail.html', context={"product": product})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    
    return redirect(reverse("product",kwargs={"slug": slug}))


def checkout(request):
    # if request.method =="POST":
    #     items = request.POST.get('items')
    #     total = request.POST.get('total')
    #     nom = request.POST.get('nom')
    #     email = request.POST.get('email')
    #     address = request.POST.get('address')
    #     ville = request.POST.get('ville')
    #     pays = request.POST.get('pays')
    #     zipcode = request.POST.get('zipcode')
    #     comman= Commande(nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode, items=items, total=total )
    #     comman.save()

    cart = get_object_or_404(Cart, user=request.user)
    return redirect ('confirmation')

    return render(request, 'product/checkout.html', context={"orders":cart.orders.all()})

def cart(request):
        cart = get_object_or_404(Cart, user=request.user)

        return render(request, 'product/cart.html', context={"orders":cart.orders.all()})

def delete_cart(request):
    cart = request.user.cart
    if cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect ('index')

def confirmation(request):
    return render(request, 'product/confirmation.html')


# Create your views here.

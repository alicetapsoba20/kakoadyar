from django.contrib.auth import settings
from django.db import models


# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=200)
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.nom

class Product(models.Model):
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    prix = models.FloatField()
    description = models.TextField()
    Categories = models.ForeignKey(Category,related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length = 5000)
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.nom

class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.nom} ({self.quantity})"


class Cart (models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        orders = models.ManyToManyField(Order)
        ordered = models.BooleanField(default=False)
        ordered_date = models.DateTimeField(blank=True, null=True)

        def __str__(self):
             return self.user.username

    


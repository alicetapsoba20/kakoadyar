# from math import prod
# from django.contrib import admin
# from .models import Agriculteur, Produit
# # class AgriculteurAdmin(admin.ModelAdmin):
# #     list_display = ('Nom','Prenom','Region','bref_description')
# admin.site.register(Agriculteur)
# admin.site.register(Produit)

from django.contrib import admin
from .models import Category,Product,Commande

# Register your models here.
admin.site.site_header = "kakaodyar"
admin.site.site_title = "kakaodyar"
admin.site.index_title = "Manageur"

class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom','date_ajout')

class AdminProduct(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'Categories', 'date_ajout')
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays', 'total', 'date_commande')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
from django.contrib import admin
from .models import Category,Product,Commande, Order, Cart

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
admin.site.register(Order)
admin.site.register(Cart)
from math import prod
from django.contrib import admin
from .models import Agriculteur, Produit
# class AgriculteurAdmin(admin.ModelAdmin):
#     list_display = ('Nom','Prenom','Region','bref_description')
admin.site.register(Agriculteur)
admin.site.register(Produit)

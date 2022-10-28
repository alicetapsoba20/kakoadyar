from django.db import models


# Create your models here.
class Agriculteur(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=100)
    Tel = models.IntegerField()
    Région = models.CharField(max_length=100)
    #Produit =
    bref_description = models.TextField()

    def __str__(self):
        return f'{self.Nom} {self.Prenom}'


class Produit(models.Model):

    Nom_produit = models.CharField(max_length=250)
    choix = [
        ('cereal','Céréal'),
        ('maraichere','Maraichere'),
        ('coton','Coton')     
    ]

    choix_maraichere = [
        ('fruit','Fruit'),
        ('legume','Légume'),     
    ]

    categorie = models.CharField(max_length=100,choices=choix,default='Cereal')
    maraichere = models.CharField(max_length=100,choices=choix_maraichere,default='Fruit')
    
    Prix = models.FloatField()
    stock = models.IntegerField()
    #Date_de_production = models.DateField()
    #Produit =
    image = models.ImageField(null = True, blank = True)

    # def __init__(self):
    #     return self.Nom

    def __str__(self):
        return f'{self.Nom_produit}'

    def imageURL(self):

         try:
            url=self.image.url

         except:
             url=''
         return url

    


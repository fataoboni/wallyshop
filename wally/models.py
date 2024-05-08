from django.db import models
from django.contrib.auth.models import User



from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Stock(models.Model):
    produit= models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return self.produit.name

from django.db import models
from .models import Product

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.product and self.sale_price:
            # Calcul du bénéfice unitaire lors de la sauvegarde de la vente
            self.profit_per_unit = self.sale_price - self.product.price
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.sale_date}"
# models.py

from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount} - {self.date}"


from django.db import models
from django.contrib.auth.models import User
from .models import Product

class Commande(models.Model):
    infouser = models.CharField(max_length=255,null=True, blank=True)
    items = models.CharField(max_length=1000,null=True, blank=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    adresse_livraison = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"Commande de {self.infouser} du {self.date_commande}"

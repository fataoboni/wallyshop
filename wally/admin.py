from django.contrib import admin

# Register your models here.
# admin.py

# admin.py

from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'updated_at')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'photo')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'sale_price', 'profit_per_unit', 'sale_date')


# admin.py


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date')
    list_filter = ('date',)
    search_fields = ('description', 'amount')







from django.contrib import admin
from .models import Category, Commande, Stock

# Créez vos configurations personnalisées pour chaque modèle

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('quantite',)

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('infouser', 'date_commande', 'items')

# Enregistrez les modèles avec leurs configurations personnalisées

admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Commande, CommandeAdmin)


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Sale, SaleAdmin)

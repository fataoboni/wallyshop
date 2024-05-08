from django.urls import path
from . import views  # Importez le module views depuis le même répertoire que urls.py
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('all', all, name='all'),
    path('offre', views.offre, name='offre'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('ajout/', views.ajout, name='ajout'),
    path('add_expense/', views.add_expense, name='add_exp   ense'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('ajouter_commande_2/', views.ajouter_commande_2, name='ajouter_commande_2'),
    path('afficher-commandes/', views.afficher_commandes, name='afficher_commandes'),
]

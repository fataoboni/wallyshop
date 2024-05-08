from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
from django.shortcuts import render
from .models import Product

from django.db.models import Q

def index(request):
    query = request.GET.get('query')
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(price__icontains=query)
        )

    return render(request, 'index.html', {'products': products})

def all(request):
    # Récupérer tous les produits de la base de données
    products = Product.objects.all()
    
    # Passer les produits au template
    return render(request, 'all.html', {'products': products})

def offre(request):
    return render(request, 'offre.html')


from django.shortcuts import render, get_object_or_404



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
from .models import Profile

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        telephone = request.POST.get('telephone')
        photo = request.FILES.get('photo')  # Récupérer le fichier de photo téléchargé
        
        # Vérifier si le nom d'utilisateur est déjà pris
        if User.objects.filter(username=username).exists():
            # Gérer le cas où le nom d'utilisateur est déjà pris
            # Par exemple, afficher un message d'erreur ou rediriger vers une page de signup avec un message d'erreur
            pass
        else:
            # Création de l'utilisateur
            user = User.objects.create_user(username=username, password=password)
            
            # Création du profil de l'utilisateur
            profile = Profile.objects.create(user=user, telephone=telephone)
            
            # Vérifier si une photo a été téléchargée
            if photo:
                # Enregistrer la photo dans le répertoire des médias
                path = default_storage.save('profile_photos/' + photo.name, photo)
                profile.photo = path
                profile.save()

            # Authentification et connexion automatique de l'utilisateur après l'inscription
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('signin')  # Rediriger vers la page d'accueil après l'inscription

    return render(request, 'signup.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Rediriger vers la page d'accueil après la connexion
        else:
            # Gérer l'échec de l'authentification, par exemple afficher un message d'erreur
            pass

    return render(request, 'signin.html')
# views.py

from django.shortcuts import render, redirect
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def ajout(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # Créer un nouvel objet Product et le sauvegarder en base de données
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image
        )
        return redirect('index')  # Redirige vers la liste des produits après ajout
    
    # Vérifier si l'utilisateur est connecté
    if not request.user.is_authenticated:
        # Rediriger vers la page de connexion
        return redirect('signin')  # Assurez-vous que 'signin' correspond à l'URL de votre page de connexion
    
    # Si l'utilisateur est connecté et la méthode de requête est GET, affiche simplement le formulaire
    return render(request, 'ajout.html')




# views.py

from django.shortcuts import render, redirect
from .models import Expense

def add_expense(request):
    if request.method == 'POST':
        # Récupération des données soumises
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        # Création de l'objet dépense dans la base de données
        Expense.objects.create(description=description, amount=amount)

        # Redirection vers une autre vue après l'ajout de la dépense
        return redirect('index')
    else:
        # Affichage du formulaire vide
        return render(request, 'ajout_depenses.html')






from django.shortcuts import render, redirect
from .models import Commande

def ajouter_commande_1(request):
    if request.method == 'POST':
        # Traitez les données du formulaire pour ajouter une commande
        infouser = request.POST.get('infouser')
        items = request.POST.get('items')
        telephone = request.POST.get('telephone')
        adresse_livraison = request.POST.get('adresse_livraison')
        Commande.objects.create(infouser=infouser, items=items, adresse_livraison=adresse_livraison,telephone=telephone)
        # Redirigez vers la page d'accueil (index) après avoir ajouté la commande
        return redirect('index')
    else:
        # Affichez le formulaire pour ajouter une commande (le template associé à cette vue devrait avoir le formulaire)
        return render(request, 'index.html')

from django.shortcuts import redirect
from .models import Commande

def ajouter_commande_2(request):
    if request.method == 'POST':
        # Traitez les données du formulaire pour ajouter une commande
        infouser = request.POST.get('infouser')
        items = request.POST.get('items')
        adresse_livraison = request.POST.get('adresse_livraison')
        Commande.objects.create(infouser=infouser, items=items, adresse_livraison=adresse_livraison)
        # Redirigez vers la page d'accueil (index) après avoir ajouté la commande
        return redirect('index')
    else:
        # Affichez le formulaire pour ajouter une commande (le template associé à cette vue devrait avoir le formulaire)
        return render(request, 'commande.html')



def product_detail(request, product_id):
    # Récupérer le produit à partir de l'ID
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})




from django.shortcuts import render
from .models import Commande

def afficher_commandes(request):
    # Récupérer toutes les commandes depuis la base de données
    commandes = Commande.objects.all()
    # Passer les commandes au template
    return render(request, 'achat.html', {'commandes': commandes})

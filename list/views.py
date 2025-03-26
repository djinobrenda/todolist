from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
from . models import *
from .forms import *

def inscription(request):
    if request.method =='POST':
        form=utilisateurForm(request.POST)
        if  form.is_valid():
            user = form.save()
            login(request, user)
            form.save()
            return redirect('liste_tache')
    else:
        form = utilisateurForm()
    return render(request, 'list/inscription.html', {'form': form})

def connexion(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_tache')
        else:
            messages.error(request,'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request,'list/connexion.html') 

def deconnexion (request):
    logout(request)
    return redirect ('connexion')


def accueil(request):
    return render(request, 'list/accueil.html')

@login_required
def liste_tache (request):
    tache = Tache.objects.filter(user=request.user)
    champ_tri= request.GET.get('tri','titre')
    ordre_tri= request.GET.get('ordre','asc')
    champs_v=['titre','date']
    if champ_tri not in champs_v:
        champ_tri = 'nom_p'
    # Préparation de l'ordre de tri (asc ou desc)
    if ordre_tri == 'desc':
        champ_tri = f'-{champ_tri}'
    tache = tache.order_by(champ_tri)

    return render(request, 'list/liste_tache.html', {'tache': tache})

@login_required
def ajouter_tache(request):
    if request.method =='POST':
        form= tacheForm(request.POST)
        if  form.is_valid():
            tache = form.save(commit=False)
            tache.user = request.user
            form.save()
            return redirect('liste_tache')
    else:
        form = tacheForm()
    return render(request, 'list/ajouter_tache.html', {'form': form})

@login_required
def modifier_tache(request,pk):
    # tache=tache.objects.get(pk=pk)
    tache = get_object_or_404(Tache, pk=pk , user=request.user)
    if request.method =='POST':
        form= tacheForm(request.POST, instance=tache)
        if  form.is_valid():
            form.save()
            return redirect('liste_tache')
    else:
        form = tacheForm(instance=tache)
    return render(request, 'list/modifier_tache.html', {'form': form})


def supprimer_tache(request,pk):
    tache=tache.objects.get(Tache,pk=pk, user=request.user)
    if request.method =='POST':
        tache.delete()
        messages.success(request, 'tache supprimée avec succès.')
        return redirect('liste_tache')
    
    return render(request, 'list/supprimer_tache.html', {'tache': tache})

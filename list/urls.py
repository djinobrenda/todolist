from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('inscription', views.inscription, name='inscription'),
    path('connexion', views.connexion, name='connexion'),
    path('accueil', views.accueil, name='accueil'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('ajouter_tache', views.ajouter_tache, name='ajouter_tache'),
    path('modifier_tache <int:pk>/', views.modifier_tache, name='modifier_tache'),
    path('supprimer_tache <int:pk>/', views.supprimer_tache, name='supprimer_tache'),
    path('', views.liste_tache, name='liste_tache'),


]

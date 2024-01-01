from django.urls import path
from app import  views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

    path('home/', views.home, name='home'),

    # Les clients
    path('clients/liste/', views.liste_client, name='liste_client'),
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('clients/modifier/<int:id>/', views.modifier_client, name='modifier_client'),
    path('clients/supprimer/<int:id>/', views.supprimer_client, name='supprimer_client'),


    # Les intervenants
    path('intervenants/liste/', views.liste_intervenant, name='liste_intervenant'),
    path('intervenants/ajouter/', views.ajouter_intervenant, name='ajouter_intervenant'),
    path('intervenants/modifier/<int:id>/', views.modifier_intervenant, name='modifier_intervenant'),
    path('intervenants/supprimer/<int:id>/', views.supprimer_intervenant, name='supprimer_intervenant'),


    
    # Les interventions
    path('interventions/liste/', views.liste_intervention, name='liste_intervention'),
    path('interventions/ajouter/', views.ajouter_intervention, name='ajouter_intervention'),
    path('interventions/modifier/<int:id>/', views.modifier_intervention, name='modifier_intervention'),
    path('interventions/supprimer/<int:id>/', views.supprimer_intervention, name='supprimer_intervention'),
]
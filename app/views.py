from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from .models import Client, Intervenant, Intervention
from .forms import ClientForm, IntervenantForm, InterventionForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Authentification
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'signin.html', {'error_message': 'Identifiants invalides.'})
    else:
        return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

#Home page
@login_required(login_url='signin')

def home(request):
    intervenants = Intervenant.objects.all()

    total_taches = Intervention.objects.count()

    taches_realisees = Intervention.objects.filter(etat='Réalisée').count()
    taches_en_attente = Intervention.objects.filter(etat='En attente').count()


    labels = []
    values = []
    for intervenant in intervenants:
        total_int = Intervention.objects.filter(etat="Réalisée", intervenant=intervenant).count()
        labels.append(f"{intervenant.nom}{intervenant.prenom}")
        values.append((total_int / taches_realisees) * 100) if taches_realisees > 0 else 0


    P_taches_realisees = taches_realisees / total_taches * 100 if total_taches > 0 else 0
    P_taches_en_attente = taches_en_attente / total_taches * 100 if total_taches > 0 else 0

    context = {
        'labels': labels,
        'values': values,
        'P_taches_realisees': P_taches_realisees,
        'P_taches_en_attente': P_taches_en_attente
    }

    return render(request, "home.html", context)

# Les clients
@login_required(login_url='signin')
def liste_client(request):
    clients = Client.objects.all()
    return render(request, "clients/liste.html", {'clients':clients})

@login_required(login_url='signin')
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client ajouté avec succès.')
            return redirect('liste_client')
    else:
        form = ClientForm()
    return render(request, 'clients/ajouter.html', {'form': form})

@login_required(login_url='signin')
def modifier_client(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.info(request, 'client modifié avec succès.')
            return redirect('liste_client')
    else:
        form = ClientForm(instance=client)

    return render(request, 'clients/modifier.html', {'form':form, 'client':client})

@login_required(login_url='signin')
def supprimer_client(request, id):
    client = get_object_or_404(Client, pk=id)
    print(client)
    client.delete()
    messages.warning(request, 'Client supprimée avec succès.')
    return redirect('liste_client')

# Les intervenanta
@login_required(login_url='signin')
def liste_intervenant(request):
    intervenants = Intervenant.objects.all()
    return render(request, "intervenants/liste.html", {'intervenants':intervenants})

@login_required(login_url='signin')
def ajouter_intervenant(request):
    if request.method == 'POST':
        form = IntervenantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Intervenant ajouté avec succès.')
            return redirect('liste_intervenant')
    else:
        form = IntervenantForm()
    return render(request, 'intervenants/ajouter.html', {'form': form})

@login_required(login_url='signin')
def modifier_intervenant(request, id):
    intervenant = get_object_or_404(Intervenant, pk=id)
    if request.method == 'POST':
        form = IntervenantForm(request.POST, instance=intervenant)
        if form.is_valid():
            form.save()
            messages.info(request, 'Intervenant modifié avec succès.')
            return redirect('liste_intervenant')  
    else:
        form = IntervenantForm(instance=intervenant)
    return render(request, 'intervenants/modifier.html', {'form':form, 'intervenant':intervenant})

@login_required(login_url='signin')
def supprimer_intervenant(request, id):
    intervenant = get_object_or_404(Intervenant, pk=id)
    intervenant.delete()
    messages.warning(request, 'Intervenant supprimée avec succès.')
    return redirect('liste_intervenant')



# Les interventions
@login_required(login_url='signin')
def liste_intervention(request):
    # Utilisez select_related pour récupérer les objets liés (intervenant, client)
    interventions = Intervention.objects.select_related('intervenant', 'client').all()  
    
    return render(request, "interventions/liste.html", {'interventions':interventions})

@login_required(login_url='signin')
def ajouter_intervention(request):
    if request.method == 'POST':
        form = InterventionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Intervention ajouté avec succès.')
            return redirect('liste_intervention')
    else:
        form = InterventionForm()
    
    intervenants = Intervenant.objects.all()
    clients = Client.objects.all()
    return render(request, "interventions/ajouter.html", {'form': form, 'intervenants': intervenants, 'clients': clients})

@login_required(login_url='signin')
def modifier_intervention(request, id):
    intervention = get_object_or_404(Intervention, pk=id)
    if request.method == 'POST':
        form = InterventionForm(request.POST, instance=intervention)
        if form.is_valid():
            form.save()
            messages.info(request, 'Intervention modifié avec succès.')
            return redirect('liste_intervention')
    else:
        form = InterventionForm(instance=intervention)
    
    intervenants = Intervenant.objects.all()
    clients = Client.objects.all()
    return render(request, 'interventions/modifier.html', {'form':form, 'intervention':intervention, 'intervenants': intervenants, 'clients': clients})

@login_required(login_url='signin')
def supprimer_intervention(request, id):
    intervention = get_object_or_404(Intervention, pk=id)
    intervention.delete()
    messages.warning(request, 'Intervention supprimée avec succès.')
    return redirect('liste_intervention')
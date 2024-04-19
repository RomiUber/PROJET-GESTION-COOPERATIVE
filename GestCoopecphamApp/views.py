from django.shortcuts import render,HttpResponseRedirect
from .forms import MemberRegistration, SavingRegistration
from .models import personne
from .models import epargne
# Create your views here.
# Cette fonction permet d'ajouter et d'afficher les information d'un cooperateur
def add_cooperator(request):
    if request.method == 'POST':
        fm = MemberRegistration(request.POST)
        if fm.is_valid():
            np = fm.cleaned_data['nom_pers']
            pp = fm.cleaned_data['prenom_pers']
            tel= fm.cleaned_data['tel_pers']
            role = fm.cleaned_data['role_pers']
            pw = fm.cleaned_data['password_pers']
            reg = personne( nom_pers = np,prenom_pers=pp,tel_pers=tel,role_pers=role,password_pers=pw)
            reg.save()
        fm = MemberRegistration()
    else:
        fm = MemberRegistration()
    coopera= personne.objects.all()
    return render(request, 'cooperator/addcooperator.html',{'form':fm,'coopera':coopera})

# Cette fonction permet de modifier les informations  d'un cooperateur

def update_data_cooperateur(request,id):
    if request.method == 'POST':
        pi= personne.objects.get(pk=id)
        fm = MemberRegistration(request.POST , instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi= personne.objects.get(pk=id)
        fm = MemberRegistration(instance=pi)
    return render(request , 'cooperator/updatecooperator.html',{'form':fm})

# Cette fonction permet de supprimer les information d'un cooperateur
def delete_data_cooperateur(request,id):
    if request.method == 'POST':
        pi = personne.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# Cette fonction permet d'ajouter  les informations  d'une epargne effectuee
def add_saving(request):
    if request.method == 'POST':
        fm = SavingRegistration(request.POST)
        print(fm.is_valid(), "------------------------------")
        print(fm.errors, "**************************")
        if fm.is_valid():
            me = fm.cleaned_data['montant_epargne']
            ap= fm.cleaned_data['ancien_solde']
            ns= fm.cleaned_data['nouveau_solde']
            de = fm.cleaned_data['Date_epargne']
            reg = epargne(montant_epargne = me ,ancien_solde=ap,nouveau_solde=ns,Date_epargne=de)
            reg.save()
    else:
        fm = SavingRegistration()
    sold= epargne.objects.all()
    return render(request, 'saving/addsaving.html',{'form':fm,'sold':sold})
    

# Cette fonction permet de modifier les information d'une epargne effectuee

def update_data_saving(request,id):
    if request.method == 'POST':
        pi= epargne.objects.get(pk=id)
        fm = SavingRegistration(request.POST , instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi= epargne.objects.get(pk=id)
        fm = SavingRegistration(instance=pi)
    return render(request , 'saving/updatesaving.html',{'form':fm})

# Cette fonction permet de supprimer les information d'une epargne effectuee
def delete_data_saving(request,id):
    if request.method == 'POST':
        pi = epargne.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')    
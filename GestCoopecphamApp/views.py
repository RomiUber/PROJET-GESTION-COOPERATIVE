from django.shortcuts import render,HttpResponseRedirect
from .forms import MemberRegistration
from .models import personne

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

def update_data(request,id):
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
def delete_data(request,id):
    if request.method == 'POST':
        pi = personne.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


    
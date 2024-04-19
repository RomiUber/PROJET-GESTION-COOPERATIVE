from django.core import validators
from django import forms
from .models import personne 
from .models import epargne

class MemberRegistration (forms.ModelForm):
    class Meta: 
        model = personne
        fields = ['nom_pers','prenom_pers','tel_pers','role_pers','password_pers']
        widgets = {
            'nom_pers': forms.TextInput ( attrs = {'class' : 'form-control'}),
            'prenom_pers': forms.TextInput( attrs = {'class':'form-control'}),
            'tel_pers' : forms.TextInput( attrs = {'class':'form-control'}),
            'role_pers' : forms.TextInput( attrs = {'class':'form-control'}),
            'password_pers': forms.PasswordInput( render_value=True, attrs = {'class':'form-control'}),
        }
        
class SavingRegistration(forms.ModelForm):
    class Meta:
        model = epargne
        fields = ['montant_epargne','ancien_solde','nouveau_solde','Date_epargne', 'id_pers']
        widgets = {
            'montant_epargne': forms.NumberInput ( attrs = {'class' : 'form-control'}),
            'ancien_solde': forms.NumberInput( attrs = {'class':'form-control'}),
            'nouveau_solde' : forms.NumberInput( attrs = {'class':'form-control'}),
            'Date_epargne' : forms.TextInput( attrs = {'class':'form-control'}),
            "id_pers":forms.Select(attrs={"class":"form-control"})
        }
                
        
        

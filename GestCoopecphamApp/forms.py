from django.core import validators
from django import forms
from .models import personne 

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
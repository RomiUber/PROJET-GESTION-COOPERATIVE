from django.contrib import admin
from .models import personne
from .models import epargne
# Register your models here.
@admin.register(personne)
class personneAdmin(admin.ModelAdmin):
    list_display = ("id","nom_pers","prenom_pers","tel_pers","role_pers","password_pers")

    
@admin.register(epargne)
class epargneAdmin(admin.ModelAdmin):
    list_display=("id_epargne","montant_epargne","ancien_solde","nouveau_solde","Date_epargne","id_pers")

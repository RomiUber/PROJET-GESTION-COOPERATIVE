from django.contrib import admin
from .models import personne
# Register your models here.
@admin.register(personne)
class personneAdmin(admin.ModelAdmin):
    list_display = ("id","nom_pers","prenom_pers","tel_pers","role_pers","password_pers")

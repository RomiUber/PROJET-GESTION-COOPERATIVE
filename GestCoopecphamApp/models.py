from django.db import models

# Create your models here.
class personne(models.Model):
    nom_pers = models.CharField(max_length = 700) 
    prenom_pers = models.CharField(max_length = 100) 
    tel_pers = models.CharField(max_length = 15) 
    role_pers = models.CharField(max_length = 15) 
    password_pers = models.CharField(max_length = 10)
    
    def __str__(self):
        return f"{self.nom_pers} {self.prenom_pers}"
class epargne(models.Model):
    id_pers = models.ForeignKey(personne, on_delete=models.CASCADE)
    id_epargne = models.AutoField(primary_key=True)
    montant_epargne = models.IntegerField()
    ancien_solde = models.IntegerField()
    nouveau_solde = models.IntegerField()
    Date_epargne = models.DateField()
    

           
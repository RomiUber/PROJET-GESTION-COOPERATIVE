from django.db import models

# Create your models here.
class personne(models.Model):
    nom_pers = models.CharField(max_length = 700) 
    prenom_pers = models.CharField(max_length = 100) 
    tel_pers = models.CharField(max_length = 15) 
    role_pers = models.CharField(max_length = 15) 
    password_pers = models.CharField(max_length = 10)
    
    
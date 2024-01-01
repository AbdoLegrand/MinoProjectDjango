from django.db import models
from datetime import datetime

# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    direction = models.CharField(max_length=50)



    
class Intervenant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Intervention(models.Model):
    date = models.DateField(default=datetime.now)
    type = models.CharField(max_length=100)
    motive = models.CharField(max_length=20)
    etat = models.CharField(max_length=20)
    intervenant = models.ForeignKey(Intervenant, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


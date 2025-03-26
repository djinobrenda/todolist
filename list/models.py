from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tache (models.Model):
    STATUS_CHOICES = [
        ('todo', 'À faire'),
        ('in_progress', 'En cours'),
        ('done', 'Terminé'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null= True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    titre= models.CharField(max_length = 100)
    description= models.TextField(blank= True, null= True)
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


class utilisateur(models.Model):
        nom= models.CharField(max_length=100)
        pwd= models.CharField(max_length=50)
from django.db import models

# Create your models here.

class Commentaire(models.Model):
    titre= models.CharField(max_length=100)
    commentaire =models.TextField(max_length=100)
    cdate=models.DateField()

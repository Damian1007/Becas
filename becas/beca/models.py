from django.db import models

# Create your models here.
class Beca(models.Model):
    id = models.AutoField(primary_key=True)
    Categoria = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=100)
    Porcentaje_F = models.IntegerField(max_length=100)
    Pais = models.CharField(max_length=100)
    Universidad = models.CharField(max_length=100)
    Requirimientos = models.CharField(max_length=100)
    Popularidad = models.IntegerField(max_length=100)
from django.db import models

# Create your models here.

class Postulante(models.Model):
    correo = models.EmailField()
    run=models.CharField(max_length=12)
    nombre=models.CharField(max_length=100)
    fechanac=models.DateField()
    telefono=models.IntegerField()
    region=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)
    tipov=models.CharField(max_length=50)


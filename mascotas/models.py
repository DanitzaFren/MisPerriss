from django.db import models

# Create your models here.


class Mascota(models.Model):
	fotografia = models.CharField(max_length=50)
	nombre = models.CharField(max_length=20)
	raza = models.CharField(max_length=40)
	desc = models.CharField(max_length=200)
	estado = models.CharField(max_length=20)


	def __str__(self):
		return self.fotografia



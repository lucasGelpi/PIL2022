from django.db import models

# Create your models here.

class Notas(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=500)
    estado=models.BooleanField()
    fecha_cierre=models.PositiveIntegerField()
   
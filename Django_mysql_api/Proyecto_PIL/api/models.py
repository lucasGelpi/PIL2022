from django.db import models

# Create your models here.

STATE_CHOICES = (
    ("PENDIENTE", "Pendiente"),
    ("EN PROCESO", "En proceso"),
    ("FINALIZADO", "Finalizado"),
)

class Notas(models.Model):
    titulo=models.CharField(max_length=50, 
                    default="Nueva nota")
    descripcion=models.CharField(max_length=500)
    estado = models.CharField(max_length=15,
                    choices=STATE_CHOICES,
                    default="PENDIENTE")
    fecha_creacion=models.PositiveIntegerField()                
    fecha_cierre=models.PositiveIntegerField()
    
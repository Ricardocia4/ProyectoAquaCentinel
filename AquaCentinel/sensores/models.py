from django.db import models
from django.contrib.auth.models import User # Importamos el modelo estándar

class Boya(models.Model):
    codigo_boya = models.CharField(max_length=100, unique=True)
    # Relación directa al modelo User de Django
    usuario = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.codigo_boya

class RegistroSensor(models.Model):
    boya = models.ForeignKey(Boya, on_delete=models.CASCADE)
    ph = models.FloatField()
    turbidez = models.FloatField()
    temperatura = models.FloatField()
    conductividad = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo estándar
from django.core.validators import MinValueValidator


class Boya(models.Model):
    codigo_boya = models.CharField(max_length=100, unique=True)
    # Relación directa al modelo User de Django
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.codigo_boya


class RegistroSensor(models.Model):
    boya = models.ForeignKey(Boya, on_delete=models.CASCADE)
    ph = models.FloatField(validators=[MinValueValidator(0.0)])
    turbidez = models.FloatField(validators=[MinValueValidator(0.0)])
    temperatura = models.FloatField(validators=[MinValueValidator(0.0)])
    conductividad = models.FloatField(validators=[MinValueValidator(0.0)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

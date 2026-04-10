from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo estándar
from django.core.validators import MinValueValidator
import uuid


class Boya(models.Model):
    # 'editable=False' lo oculta de los formularios por defecto
    class Meta:
        db_table = "sensores_boya"

    codigo_boya = models.CharField(max_length=100, unique=True, editable=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Solo generamos el código si la boya es nueva (no tiene ID aún)
        if not self.pk and not self.codigo_boya:
            # Genera un código único basado en UUID (ej: AQUA-A1B2C3D4)
            nuevo_id = str(uuid.uuid4()).split("-")[0].upper()
            self.codigo_boya = f"AQUA-{nuevo_id}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo_boya


class RegistroSensor(models.Model):

    boya = models.ForeignKey(Boya, on_delete=models.CASCADE)
    ph = models.FloatField(validators=[MinValueValidator(0.0)])
    turbidez = models.FloatField(validators=[MinValueValidator(0.0)])
    temperatura = models.FloatField(validators=[MinValueValidator(0.0)])
    conductividad = models.FloatField(validators=[MinValueValidator(0.0)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

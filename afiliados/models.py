
from django.db import models

class Afiliado(models.Model):
    numero_afiliado = models.CharField(max_length=20, unique=True)
    apellido_nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)
    SECTOR_CHOICES = [
        ('Norte', 'Norte'),
        ('Sur', 'Sur'),
        ('Este', 'Este'),
        ('Oeste', 'Oeste'),
        ('Centro', 'Centro'),
    ]
    sector = models.CharField(max_length=20, choices=SECTOR_CHOICES)
    horario = models.TimeField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    hecho = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero_afiliado} - {self.apellido_nombre}"

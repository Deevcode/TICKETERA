from django.db import models
from .opciones import SEDE_CHOICES, MODALIDAD_CHOICES, REPORTE_CHOICES

class Ticket(models.Model):
    IdTicket = models.AutoField(primary_key=True)
    Sede = models.IntegerField(choices=SEDE_CHOICES, null=True)
    Direccion = models.CharField(max_length=200)
    Area = models.CharField(max_length=200)
    Modalidad = models.IntegerField(choices=MODALIDAD_CHOICES, null=True)
    Nombre = models.CharField(max_length=200)
    Rut = models.CharField(max_length=12)
    Usuario = models.CharField(max_length=200)
    CorreoInstitucional = models.EmailField()
    Telefono = models.CharField(max_length=12)
    FechaEmision = models.DateTimeField(auto_now_add=True)
    TipoReporte = models.IntegerField(choices=REPORTE_CHOICES, null=True)
    Solicitud = models.CharField(max_length=600, default='')
    IP = models.CharField(max_length=200, blank=True, null=True)
    HOSTNAME = models.CharField(max_length=200, blank=True, null=True)
    MARCA_MODELO = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.IdTicket} ; {self.Usuario} ; {self.FechaEmision}"

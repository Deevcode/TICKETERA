from django.db import models

SEDE_CHOICES = [
    (0, "Casa Central"),
    (1, "Hospital del trabajador [HT]"),
    (2, "Centro Medico [CEM]"),
    (3, "ESACHS [Ramon Carnicer 151]"),
    (4, "Rancagua 333"),
    (5, "OTEC"),
    (6, "ESE-CENTRO DE COMANDO [TERRENO]")
]

MODALIDAD_CHOICES = [
    (0, "PRESENCIAL"),
    (1, "TELETRABAJO")
]

REPORTE_CHOICES = [
    (0, "INCIDENCIA"),
    (1, "REQUERIMIENTO")
]
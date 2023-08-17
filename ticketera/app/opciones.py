from django.db import models

SEDE_CHOICES = [
    (0, "--SELECCIONE UNA SEDE--"),
    (1, "Hospital del trabajador [HT]"),
    (2, "Centro Medico [CEM]"),
    (3, "ESACHS [Ramon Carnicer 151]"),
    (4, "Rancagua 333"),
    (5, "OTEC"),
    (6, "ESE-CENTRO DE COMANDO [TERRENO]"),
    (7, "Casa Central")
]

MODALIDAD_CHOICES = [
    (0, "--SELECCIONE MODALIDAD--"),
    (1, "TELETRABAJO"),
    (1, "PRESENCIAL")
]

REPORTE_CHOICES = [
    (0, "--SELECCION DE REPORTE--"),
    (1, "INCIDENCIA"),
    (2, "REQUERIMIENTO")
]
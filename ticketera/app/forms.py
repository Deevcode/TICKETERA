from django import forms
from .opciones import SEDE_CHOICES, MODALIDAD_CHOICES, REPORTE_CHOICES

class TicketForm(forms.Form):
    Sede = forms.ChoiceField(choices=SEDE_CHOICES, required=True)
    Direccion = forms.CharField(max_length=200, required=True)
    Area = forms.CharField(max_length=200, required=True)
    Modalidad = forms.ChoiceField(choices=MODALIDAD_CHOICES, required=True)
    Nombre = forms.CharField(max_length=200, required=True)
    Rut = forms.CharField(max_length=12, required=True)
    Usuario = forms.CharField(max_length=200, required=True)
    CorreoInstitucional = forms.EmailField(required=True)
    Telefono = forms.CharField(max_length=12, required=True)
    TipoReporte = forms.ChoiceField(choices=REPORTE_CHOICES, required=True)
    Solicitud = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)
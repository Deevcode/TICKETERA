from django import forms
from .models import *

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
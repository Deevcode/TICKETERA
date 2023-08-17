from django.contrib import admin
from .models import *
# Register your models here.
#ADMIN DE REGION
class TicketAdmin(admin.ModelAdmin):
    list_display = ("IdTicket","Sede","Direccion","Area","Modalidad","Nombre","Rut","Usuario","CorreoInstitucional","Telefono","FechaEmision","TipoReporte","Solicitud")
    search_fields = ["Usuario"]

admin.site.register(Ticket, TicketAdmin)
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def registrar_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = Ticket(
                Sede=form.cleaned_data['Sede'],
                Direccion=form.cleaned_data['Direccion'],
                Area=form.cleaned_data['Area'],
                Modalidad=form.cleaned_data['Modalidad'],
                Nombre=form.cleaned_data['Nombre'],
                Rut=form.cleaned_data['Rut'],
                Usuario=form.cleaned_data['Usuario'],
                CorreoInstitucional=form.cleaned_data['CorreoInstitucional'],
                Telefono=form.cleaned_data['Telefono'],
                TipoReporte=form.cleaned_data['TipoReporte'],
                Solicitud=form.cleaned_data['Solicitud']
            )
            ticket.save()
            return redirect('exito')  # Cambia 'exito' por la URL correcta
    else:
        form = TicketForm()

    return render(request, 'app/registrar_ticket.html', {'form': form})

def listar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'app/listar_tickets.html', {'tickets': tickets})

def exito(request):
    return render(request, 'app/exito.html')

def editar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            # Actualizar los campos del ticket con los datos del formulario
            ticket.Sede = form.cleaned_data['Sede']
            ticket.Direccion = form.cleaned_data['Direccion']
            # Agrega más campos aquí

            ticket.save()
            return redirect('listar_tickets')  # Cambia 'listar_tickets' por la URL correcta
    else:
        # Inicializar el formulario con los datos del ticket
        form = TicketForm(initial={
            'Sede': ticket.Sede,
            'Direccion': ticket.Direccion,
            # Agrega más campos aquí
        })

    return render(request, 'app/editar_ticket.html', {'form': form, 'ticket': ticket})
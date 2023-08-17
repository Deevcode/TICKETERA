from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('registrar-ticket/', registrar_ticket, name='registrar_ticket'),
    path('listar-tickets/', listar_tickets, name='listar_tickets'),
    path('exito/', exito, name='exito'),
    path('editar-ticket/<int:ticket_id>/', editar_ticket, name='editar_ticket'),
]
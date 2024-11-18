from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Ticket
from .forms import TicketForm


def ticket_list(request):
    tickets = Ticket.objects.all()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            # Create new ticket
            Ticket.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
    else:
        form = TicketForm()
    return render(request, 'ticket_list.html', {'tickets': tickets, "form": form})


def edit_ticket(request, id):
    tickets = Ticket.objects.all()
    ticket = Ticket.objects.get(pk=id)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticket_edit.html', {'tickets': tickets, "form": form})

def delete_ticket(request, id):
    tickets = Ticket.objects.all()
    ticket = Ticket.objects.get(pk=id)
    ticket.delete()
    return HttpResponseRedirect('/')
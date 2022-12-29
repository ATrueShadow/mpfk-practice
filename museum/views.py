from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
import users.models
from .models import Tour, Ticket, Exhibition, Item
from django.shortcuts import get_object_or_404


# Create your views here.


class ToursIndexListView(generic.ListView):
    model = Tour
    context_object_name = 'tour_list'
    template_name = 'index.html'


class TourIndexDetailView(generic.DetailView):
    model = Tour
    template_name = 'tour_detail.html'


class ToursListView(generic.ListView):
    model = Tour
    context_object_name = 'tour_list'
    template_name = 'tours.html'


class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'tour-manage.html'


class TourUpdateView(generic.UpdateView):
    model = Tour
    template_name = 'tour_update.html'
    fields = ['name', 'exhibitions', 'date', 'admission', 'price']


class TourDeleteView(generic.DeleteView):
    model = Tour
    template_name = 'tour-delete.html'
    success_url = 'museum/tours/'


class TourNewView(generic.CreateView):
    model = Tour
    template_name = 'tour-new.html'
    fields = ['name', 'exhibitions', 'date', 'admission', 'price']


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class TicketListView(generic.ListView):
    model = Ticket
    context_object_name = 'ticket_list'
    template_name = 'tickets.html'


class TicketDetailView(generic.DetailView):
    model = Ticket
    template_name = 'ticket-manage.html'


class TicketNewView(generic.CreateView):
    model = Ticket
    template_name = 'ticket-new.html'
    fields = ['tour', 'visitor']


class TicketUpdateView(generic.UpdateView):
    model = Ticket
    template_name = 'ticket-update.html'
    fields = ['tour', 'visitor']


class TicketDeleteView(generic.DeleteView):
    model = Ticket
    template_name = 'ticket-delete.html'
    success_url = 'museum/tickets/'


class ExhibitionListView(generic.ListView):
    model = Exhibition
    context_object_name = 'exhibition_list'
    template_name = 'exhibitions.html'


class ExhibitionDetailView(generic.DetailView):
    model = Exhibition
    template_name = 'exhibition-manage.html'


class ExhibitionUpdateView(generic.UpdateView):
    model = Exhibition
    template_name = 'exhibition-update.html'
    fields = ['name', 'items', 'tours']


class ExhibitionNewView(generic.CreateView):
    model = Exhibition
    template_name = 'exhibition-new.html'
    fields = ['name', 'items', 'tours']


class ExhibitionDeleteView(generic.DeleteView):
    model = Exhibition
    template_name = 'exhibition-delete.html'
    success_url = 'museum/exhibitions/'


class StorageListView(generic.ListView):
    model = Item
    template_name = 'storage.html'
    context_object_name = 'items_list'


class StorageDetailView(generic.DetailView):
    model = Item
    template_name = 'storage-manage.html'


class StorageUpdateView(generic.UpdateView):
    model = Item
    template_name = 'storage-update.html'
    fields = ['name', 'quantity']


class StorageDeleteView(generic.DeleteView):
    model = Item
    template_name = 'storage-delete.html'
    success_url = 'museum/storage/'


class StorageNewView(generic.CreateView):
    model = Item
    template_name = 'storage-new.html'
    fields = ['name', 'quantity']


class BuyTicketView(LoginRequiredMixin, generic.CreateView):
    login_url = 'register'
    model = Ticket
    template_name = 'ticket-buy.html'
    fields = ['tour']

    def form_valid(self, form):
        visitor = self.request.user
        form.instance.visitor = visitor
        return super(BuyTicketView, self).form_valid(form)

    def get_success_url(self):
        return reverse('tickets')

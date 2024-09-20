from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import ContactForm




def home(request):
    return render(request, 'home.html')


def info(request):
    return render(request, 'biz_haqimizda.html')

def product(request):
    return render(request, 'product.html')

class KaridorListView(ListView):
    model = Karidor
    context_object_name = 'products'
    template_name = 'karidor.html'


class OfisListView(ListView):
    model = Ofis
    context_object_name = 'products'
    template_name = 'ofis.html'


class OshxonaListView(ListView):
    model = Oshxona
    context_object_name = 'products'
    template_name = 'oshxona.html'


class ShkafListView(ListView):
    model = Shkaf
    context_object_name = 'products'
    template_name = 'shkaf.html'


class BolalarListView(ListView):
    model = Bolalar
    context_object_name = 'products'
    template_name = 'bolalar.html'

class KattalarListView(ListView):
    model = Kattalar
    context_object_name = 'products'
    template_name = 'kattalar.html'

class TvListView(ListView):
    model = Tv
    context_object_name = 'products'
    template_name = 'tv.html'

class ContactView(CreateView):
    success_url = '/'
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Warga
# Create your views here.


class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

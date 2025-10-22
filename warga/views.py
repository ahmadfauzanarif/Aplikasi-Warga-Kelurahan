from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Warga,Pengaduan
# Create your views here.


class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'
    ordering = ['-tanggal_lapor']  # urutkan dari yang terbaru


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

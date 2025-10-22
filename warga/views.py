from django.shortcuts import render
from django.urls import reverse_lazy    
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Warga,Pengaduan
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import WargaSerializer
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

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list') # Arahkan ke daftar warga setelah sukses

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' # Kita pakai template yang sama
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    fields = ['judul', 'deskripsi', 'status', 'pelapor']
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDetailView(DetailView):
    model = Pengaduan
    template_name = 'warga/pengaduan_detail.html'
    context_object_name = 'pengaduan'

# --- API VIEWS ---
class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaCreateAPIView(CreateAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
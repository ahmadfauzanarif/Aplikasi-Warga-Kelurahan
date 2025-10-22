from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanListView, WargaCreateView, PengaduanCreateView, WargaUpdateView, WargaDeleteView, PengaduanDeleteView, PengaduanUpdateView, PengaduanDetailView

urlpatterns = [
    path('', WargaListView.as_view(), name = 'warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name = 'warga-detail'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), # URL untuk form tambah
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'), # URL untuk edit
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'), # URL untuk hapus
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
    path('pengaduan/<int:pk>/', PengaduanDetailView.as_view(), name='pengaduan-detail'),
]
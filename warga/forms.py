from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        # Tentukan field mana saja dari model yang ingin ditampilkan di form
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['judul', 'deskripsi', 'status', 'pelapor']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan judul pengaduan'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tuliskan deskripsi pengaduan...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'pelapor': forms.Select(attrs={'class': 'form-control'}),
        }

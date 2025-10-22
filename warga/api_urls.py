# warga/api_urls.py
from django.urls import path
from .views import WargaListAPIView, WargaCreateAPIView, WargaDetailAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/tambah/', WargaCreateAPIView.as_view(), name='warga-create'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='warga-detail'),
]

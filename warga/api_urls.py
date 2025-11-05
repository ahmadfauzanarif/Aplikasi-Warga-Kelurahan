# warga/api_urls.py
from django.urls import path, include
# from .views import WargaListAPIView, WargaCreateAPIView, WargaDetailAPIView
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet, LoginViewSet

# Buat sebuah router dan daftarkan ViewSet kita
router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')
router.register('login', LoginViewSet, basename='login')

# URL API sekarang ditentukan secara otomatis oleh router.
urlpatterns = [
    # path('', api_root, name='api-root'),   # ⬅️ ini baris penting!
    path('', include(router.urls)),
]



# urlpatterns = [
#     path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
#     path('warga/tambah/', WargaCreateAPIView.as_view(), name='api-warga-create'),
#     path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
# ]

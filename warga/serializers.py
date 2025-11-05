# warga/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['id', 'judul', 'deskripsi', 'status', 'tanggal_lapor']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is inactive.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Username and password required.")
        return data
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e04596fc-0e49-4a36-be08-e186128c42a9" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/7dc0456f-be85-41de-82f6-5c7e11b929b0" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/dbea4925-6007-4c1b-9dc2-d855c7384445" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/40db102d-d9e1-47e4-83f5-be7477332d00" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/d797c660-776b-45b3-bc8c-5927f4114d5d" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/19d3c75e-3ef3-4aed-8ac8-73c74177116f" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/4f301b81-62c0-4c19-b5e2-d8612ef5dfd3" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/80c200dc-a5f6-4fc8-8277-9e42b7416529" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/008c6206-04d6-486f-acd4-22380c2fa19f" />

# 🏙️ Aplikasi Warga Kelurahan

Aplikasi ini dibuat menggunakan **Django Framework** dengan integrasi **Django Unfold** sebagai tema admin modern.  
Tujuannya adalah membantu pengelolaan data warga kelurahan dengan antarmuka yang sederhana, efisien, dan mudah dikembangkan.

---

## 🚀 Fitur Utama
- ✅ **CRUD Data Warga**
  - Tambah, ubah, hapus, dan lihat detail data warga.
- ✅ **CRUD Data Pengaduan**
  - Pengaduan terhubung dengan data warga (relasi *ForeignKey*).
  - Tiap warga dapat memiliki banyak pengaduan.
- ✅ **Integrasi Tema Django Unfold**
  - Tampilan admin modern dan responsif.
- ✅ **Database SQLite**
  - Simpel, tanpa konfigurasi tambahan, langsung siap pakai.
- ✅ **REST API dengan Django REST Framework (DRF)**
  - Endpoint API untuk manajemen data warga.

---

## ⚙️ API Endpoint

| Endpoint | Method | Deskripsi |
|-----------|---------|-----------|
| `/api/warga/` | **GET** | Menampilkan daftar semua warga |
| `/api/warga/tambah/` | **POST** | Menambahkan data warga baru |
| `/api/warga/<id>/` | **GET** | Menampilkan detail warga berdasarkan ID |

💡 Contoh:
```bash
GET http://127.0.0.1:8000/api/warga/1/

```
# 🧰 Teknologi yang Digunakan
| Komponen                        | Deskripsi                                       |
| ------------------------------- | ----------------------------------------------- |
| **Django**                      | Framework utama untuk pengembangan aplikasi web |
| **Django REST Framework (DRF)** | Untuk pembuatan endpoint API                    |
| **Django Unfold**               | Tema admin modern dan elegan                    |
| **SQLite**                      | Database default yang ringan dan portabel       |
| **Python 3.11+**                | Bahasa pemrograman utama                        |

#💻 Cara Menjalankan Project
# 1️⃣ Clone repositori
git clone https://github.com/ahmadfauzanarif/Aplikasi-Warga-Kelurahan.git
cd Aplikasi-Warga-Kelurahan

# 2️⃣ Aktifkan virtual environment (jika belum)
python -m venv env
env\Scripts\activate  # untuk Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Jalankan server
python manage.py runserver

Akses di browser:

Admin Panel → http://127.0.0.1:8000/admin/
Daftar Warga → http://127.0.0.1:8000/warga/
API Warga → http://127.0.0.1:8000/api/warga/

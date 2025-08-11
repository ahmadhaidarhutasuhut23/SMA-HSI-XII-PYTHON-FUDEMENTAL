# jawaban no 1

judul = input("Masukkan judul buku: ")

judul_bersih = judul.strip().title()

print("Judul yang distandarisasi:", judul_bersih)

# jawaban no 2

email = input("Masukkan alamat email: ")

if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tidak valid")

# jawaban no 3


kalimat = input("Masukkan kalimat: ")
kata_sensor = input("Masukkan kata yang ingin disensor: ")

kalimat_sensor = kalimat.replace(kata_sensor, "***")

print("Hasil kalimat setelah disensor:", kalimat_sensor)


#jawaban no 4

nama_organisasi = input("Masukkan nama organisasi: ")

kata_kata = nama_organisasi.split()
huruf_awal = [kata[0].upper() for kata in kata_kata]

akronim = ''.join(huruf_awal)

print("Akronim:", akronim)

# jawaban no 5

import re

judul = input("Masukkan judul artikel: ")

# Ubah ke huruf kecil
judul = judul.lower()

# Ganti spasi dengan tanda hubung
judul = judul.replace(" ", "-")

# Hapus semua karakter selain huruf, angka, dan tanda hubung
slug = re.sub(r'[^a-z0-9\-]', '', judul)

print("Slug URL:", slug)



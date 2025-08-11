# latihan 1

# Membuat / membuka file log_kegiatan.txt dalam mode append ('a')
# Mode 'a' artinya jika file sudah ada, kita akan menambahkan data di akhir file tanpa menghapus isinya

# 1. Buka file dalam mode append
file = open("log_kegiatan.txt", "a")

# 2. Minta input dari pengguna
kegiatan = input("Masukkan kegiatan yang baru saja dilakukan: ")

# 3. Tulis kegiatan ke file, pastikan di baris baru
file.write(kegiatan + "\n")

# 4. Tutup file untuk menyimpan perubahan
file.close()

print("Kegiatan berhasil dicatat di log_kegiatan.txt")


# latihan 2

# Program untuk menyalin isi dari sumber.txt ke salinan.txt

# 1. Buka file sumber.txt dalam mode baca
with open("sumber.txt", "r") as sumber:
    # 2. Baca seluruh isi file
    isi = sumber.read()

# 3. Buka file salinan.txt dalam mode tulis
with open("salinan.txt", "w") as salinan:
    # 4. Tulis isi yang sudah dibaca ke salinan.txt
    salinan.write(isi)

print("File berhasil disalin dari sumber.txt ke salinan.txt")


# latihan 3

import os

# 1. Minta nama file
nama_file = input("Masukkan nama file yang ingin dihapus: ")

# 2. Cek apakah file ada
if os.path.exists(nama_file):
    konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ")
    if konfirmasi.lower() == 'y':
        os.remove(nama_file)
        print(f"File '{nama_file}' berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
else:
    print(f"File '{nama_file}' tidak ditemukan.")

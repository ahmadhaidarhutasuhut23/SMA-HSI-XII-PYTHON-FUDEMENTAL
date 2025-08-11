def buat_email(nama_pengguna, domain="coding.com"):
    # Gabungkan nama pengguna dan domain, lalu ubah ke huruf kecil
    email = f"{nama_pengguna}@{domain}".lower()
    return email

# Contoh pemanggilan fungsi
print(buat_email("Budi"))               # Output: budi@coding.com
print(buat_email("Ani", "belajar.id"))  # Output: ani@belajar.id

# Latihan 2
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan}, Berat: {berat_kg}kg, Asuransi: {asuransi}, Express: {express}")

# Memanggil fungsi menggunakan keyword arguments
kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)

# Latihan 3
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

# Memanggil dan unpack hasil
hasil_total, jumlah, rata = analisis_daftar([10, 20, 30, 40, 50])
print(f"Total: {hasil_total}, Jumlah Elemen: {jumlah}, Rata-rata: {rata}")

# latihan 4
def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka untuk mendapatkan total, jumlah elemen, dan rata-rata.

    Args:
        daftar_angka (list of int or float): Daftar angka yang ingin dianalisis.

    Returns:
        tuple: Berisi tiga nilai:
            - Total (int/float): Jumlah semua angka.
            - Jumlah Elemen (int): Banyaknya elemen dalam daftar.
            - Rata-rata (float): Nilai rata-rata dari semua angka.
    """
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

# Mengecek dokumentasi
help(analisis_daftar)

# Latihan 5
# Versi biasa
def get_luas_lingkaran(radius):
    return 3.14159 * (radius ** 2)

# Versi lambda
luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)

# Uji coba
print(luas_lingkaran_lambda(7))  # Output: 153.93791

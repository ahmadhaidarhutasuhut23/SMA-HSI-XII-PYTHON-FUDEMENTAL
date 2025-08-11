# jawaban no 1
def buat_email(nama_pengguna, domain="coding.com"):
    return f"{nama_pengguna.lower()}@{domain.lower()}"

# Contoh pemanggilan
print(buat_email("Budi"))         # Output: budi@coding.com
print(buat_email("Ani", "belajar.id"))  # Output: ani@belajar.id

# jawaban no 2

def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan} dengan berat {berat_kg} kg. Express: {express}, Asuransi: {asuransi}")

# Pemanggilan dengan keyword arguments
kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)

# jawaban no 3

def analisis_daftar(daftar):
    total = sum(daftar)
    jumlah = len(daftar)
    rata_rata = total / jumlah if jumlah != 0 else 0
    return total, jumlah, rata_rata

# Pemanggilan dan unpack hasil
data = [10, 20, 30, 40, 50]
total, jumlah, rata_rata = analisis_daftar(data)

# Cetak hasil
print(f"Total: {total}")
print(f"Jumlah Elemen: {jumlah}")
print(f"Rata-rata: {rata_rata}")

# jawaban no 4

def analisis_daftar(daftar):
    """
    Menganalisis sebuah daftar angka untuk mendapatkan total, jumlah elemen, dan rata-rata.

    Args:
        daftar (list): Daftar berisi angka-angka (integer atau float).

    Returns:
        tuple: Tiga nilai, yaitu total jumlah angka, jumlah elemen, dan rata-rata dari angka-angka tersebut.
    """
    total = sum(daftar)
    jumlah = len(daftar)
    rata_rata = total / jumlah if jumlah != 0 else 0
    return total, jumlah, rata_rata

# Cek docstring
help(analisis_daftar)

# jawaban no 5

# Fungsi lambda untuk luas lingkaran
luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)

# Uji coba
print(luas_lingkaran_lambda(7))  # Output: sekitar 153.93791

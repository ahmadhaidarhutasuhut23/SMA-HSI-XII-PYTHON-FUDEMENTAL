# Selamat datang
print("=" * 43)
print("SELAMAT DATANG DI PROGRAM KASIR CERDAS!")
print("=" * 43)

# --- Input Barang 1 ---
print("\n--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan (Rp): "))
jumlah_1 = int(input("Jumlah: "))

# --- Input Barang 2 ---
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan (Rp): "))
jumlah_2 = int(input("Jumlah: "))

# --- Perhitungan Total per Barang ---
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2

# --- Subtotal ---
subtotal = total_1 + total_2

# --- Logika Diskon ---
diskon = 0.0
persen_diskon = 0

if subtotal > 200_000:
    persen_diskon = 10
elif subtotal > 100_000:
    persen_diskon = 5

diskon = subtotal * (persen_diskon / 100)
total_akhir = subtotal - diskon

# --- Cetak Struk ---
print("\nMenghitung total...")
print("=" * 43)
print("         STRUK PEMBELIAN ANDA")
print("=" * 43)
print("Detail Belanja:")

print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("-" * 43)
print(f"Subtotal         : Rp {subtotal}")
print(f"Diskon ({persen_diskon}%)     : - Rp {diskon}")
print("-" * 43)
print(f"Total yang harus dibayar: Rp {total_akhir}")
print("=" * 43)
print("     TERIMA KASIH TELAH BERBELANJA!")
print("=" * 43)


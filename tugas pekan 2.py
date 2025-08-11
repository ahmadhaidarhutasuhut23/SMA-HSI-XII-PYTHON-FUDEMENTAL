# 1 fungsi tambahan (bonus)

def get_numeric_input(prompt) :
    while true:
       try:
           
           value = float(input(prompt))
           return value
       except ValueError:
           print("input tidak valid. masukan angka yang benar .")


def format_rupiah(angka):
    return f"Rp {angka:, 2f}",replace (",",".").replace(".", ",", 1)



# 2 fungsi-fungsi utama

def tampilkan_header():
    print("=" * 43)
    print("SELAMAT DATANG DI TOKO SERBAGUNA")
    print("=" * 43)


def hitung_diskon(subtotal):
    if subtotal>= 500_000
        persen = 10
    elif subtotal >= 300_000
          persen = 5
    else:
        persen = 0
    jumlah_diskon = subtotal * ( persen / 100)
    return jumlah_diskon, persen

def tampilkan_struk(nama_barang, harga_barang, jumlah_barang, subtotal, total_diskon, persen_diskon):
    print("=" * 43)
    print(" STRUK PEMBELIAN ANDA")
    print("=" * 43)
    PRINT("Detail Belanja")

    for i in range(len(nama_barang)):
        total = harga_barang [i] * jumlah_barang[i]
        print(f"{i+1}. {nama_barang[i]} ({jumlah_barang[i]} x {format_rupiah(harga_barang[i])}) = {format_rupiah(total)}")

    
    print("=" * 43)
    print(f"Subtotal : {format_rupiah (subtotal)}")
    print(f" Diskon ({persen_diskon}%) : - {format_rupiah(total_diskon)}")
    print("=" * 43)
    print(f"Total yang harus dibayar: {format_rupiah(subtotal - total_diskon)})
    print("=" * 43)
    print(" TERIMA KASIH TELAH BERBELANJA!")
    print("=" * 43)


# no 3 program utama

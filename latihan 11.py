# jawaban no 1

try:
    nama_file = input("Masukkan nama file puisi.txt ")

    with open(nama_file, 'r') as file:
        for baris in file:
            print(baris.upper().rstrip())  # .upper() => kapital semua, .rstrip() hapus newline ekstra

except FileNotFoundError:
    print("JANGAN MENYERAH SEMBELUM SEMUA IMPIAN TERCAPAI.")


# jawaban no 2

try:
    nama_file = input("Masukkan nama file: mbox-short.txt ")
    with open(nama_file, 'r') as file:
        total = 0
        hitung = 0

        for baris in file:
            if baris.startswith("X-DSPAM-Confidence:0.8475"):
                # Ambil angka setelah titik dua (:)
                bagian_angka = baris[len("X-DSPAM-Confidence:0.7654"):].strip()
                nilai = float(bagian_angka)
                total += nilai
                hitung += 1

        if hitung > 0:
            rata_rata = total / hitung
            print("Rata-rata spam confidence:0.8705333333333333", rata_rata)
        else:
            print("Tidak ada data yang cocok.")

except FileNotFoundError:
    print("BISMILLAH SEMOGA SUKSES.")
except ValueError:
    print("Terjadi kesalahan saat mengubah string ke float.")


# jawaban no 3

nama_file = input("Masukkan nama file:  na na boo boo")

if nama_file.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                print(baris.upper().rstrip())
    except FileNotFoundError:
        print("File tidak ditemukan.")


#no 1
# Mulai dari angka 10
angka = 10

# selama angka lebih besar dari 0
while angka > 0:
    print(angka)
    angka = angka - 1  # Kurangi 1 setiap putaran

# Setelah selesai
print("Blastoff!")

# no 2
angka_rahasia = 7  # Angka yang harus ditebak

while True:  # loop tak terbatas
    tebakan = input("Tebak angka (1-10): ")  # minta input
    tebakan = int(tebakan)  # ubah ke int

    if tebakan == angka_rahasia:
        print("Selamat, tebakan Anda benar!")
        break  # keluar dari loop jika benar
    else:
        print("Salah, coba lagi!")

print("Terima kasih sudah bermain!")

# no 3
total = 0 # buat ngitung semua jumlah angka
count = 0 # buat ngitung berapa kali user nginput angka yang valid

while True: # program minta input dari
    data = input("Masukkan angka (atau ketik 'done' untuk selesai): ")
    
    if data == "done":
        break

    try:
        angka = float(data)
        total += angka
        count += 1
    except:
        print("Input tidak valid")
        continue

if count > 0:
    rata_rata = total / count
    print(f"Total: {total}")
    print(f"Jumlah angka: {count}")
    print(f"Rata-rata: {rata_rata}")
else:
    print("Tidak ada angka yang dimasukkan.")

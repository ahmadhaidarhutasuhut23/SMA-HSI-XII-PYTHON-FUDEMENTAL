# no 1

s = "Belajar Python itu Menyenangkan"

# Karakter pertama
print("Karakter pertama:", s[0])

# Karakter terakhir (indexing negatif)
print("Karakter terakhir:", s[-1])

# Karakter spasi pertama
print("Spasi pertama:", s[7])

# no 2

s = "Belajar Python itu Menyenangkan"

# "Python" dimulai dari index 8 sampai 14 (tidak termasuk 14)
print("Python:", s[8:14])

# "Menyenangkan" dimulai dari index 19 hingga akhir
print("Menyenangkan:", s[19:])

# "Belajar" adalah dari index 0 sampai 7
print("Belajar:", s[0:7])

# no 3

kata = input("Masukkan sebuah kata: ")
kata_terbalik = kata[::-1]

print("Kata setelah dibalik:", kata_terbalik)

if kata == kata_terbalik:
    print("Ini adalah palindrom!")
else:
    print("Bukan palindrom.")

# no 4
kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
kode_rahasia = kalimat[::3]
print("Kode rahasia:", kode_rahasia)

# no 5

nama_salah = "dUDI sANTOSO"

# Ambil huruf satu per satu lalu gabungkan dengan perbaikan
nama_benar = "B" + nama_salah[1:4].lower() + " " + nama_salah[5].upper() + nama_salah[6:].lower()

print("Nama benar:", nama_benar)

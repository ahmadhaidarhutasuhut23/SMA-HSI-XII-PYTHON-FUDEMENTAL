# jawaban no 1

# Meminta input jam kerja dan tarif per jam dari pengguna
jam = float(input("Masukkan jumlah jam kerja: "))
tarif = float(input("Masukkan tarif per jam: "))

# Hitung upah
if jam <= 40:
    upah = jam * tarif
else:
    lembur = jam - 40
    upah = (40 * tarif) + (lembur * tarif * 1.5)

print("Pay:", upah)

# latihan no 2
try:
    jam = float(input("Masukkan jumlah jam kerja: "))
    tarif = float(input("Masukkan tarif per jam: "))

    if jam <= 40:
        upah = jam * tarif
    else:
        lembur = jam - 40
        upah = (40 * tarif) + (lembur * tarif * 1.5)

    print("Pay:", upah)

except:
    print("Error, please enter numeric input")
 # latihan no 3
try:
    skor = float(input("Masukkan skor antara 0.0 sampai 1.0: "))

    if skor < 0.0 or skor > 1.0:
        print("Bad score")
    elif skor >= 0.9:
        print("Grade: A")
    elif skor >= 0.8:
        print("Grade: B")
    elif skor >= 0.7:
        print("Grade: C")
    elif skor >= 0.6:
        print("Grade: D")
    else:
        print("Grade: F")

except:
    print("Error, please enter numeric input")

    # latihan no 4

    # Uji coba data pengunjung
tinggi_cm = 155
usia = 10
didampingi_ortu = True

# Logika syarat masuk
if tinggi_cm >= 157 and (usia > 16 or didampingi_ortu):
    print("Boleh Masuk")
else:
    print("Tidak Boleh Masuk")


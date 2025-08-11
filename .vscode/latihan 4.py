# latihan 1
jam = float(input("Masukkan jumlah jam kerja: "))
tarif = float(input("Masukkan tarif per jam: "))

if jam <= 40:
    total_upah = jam * tarif
else:
    lembur = jam - 40
    total_upah = (40 * tarif) + (lembur * tarif * 1.5)

print(f"Pay: {total_upah}")

# Latihan 2
try:
    jam = float(input("Masukkan jumlah jam kerja: "))
    tarif = float(input("Masukkan tarif per jam: "))
    
    if jam <= 40:
        total_upah = jam * tarif
    else:
        lembur = jam - 40
        total_upah = (40 * tarif) + (lembur * tarif * 1.5)

    print(f"Pay: {total_upah}")

except:
    print("Error, masukkan dengan nomer")
# Latihan 3
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
    print("Error,silahkan masukkan input angka ")

# Latihan 4
tinggi_cm = 155
usia = 11
didampingi_ortu = True

if tinggi_cm >= 150 and (usia > 12 or didampingi_ortu):
    print("Boleh Masuk")
else:
    print("Tidak Boleh Masuk")
    print("Anda belum masuk kriteria")

# no 1 

for i in range(0, 71, 7):
    print(i)

# no 2
kalimat = "Python"
kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik
print(kalimat_terbalik)
 
 # no 3 
  
jumlah = 0

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        jumlah += 1

print("Jumlah angka yang habis dibagi 3 dan 5:", jumlah)

# no 4

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# no 5

n = int(input("Masukkan angka: "))
hasil_faktorial = 1

for i in range(1, n + 1):
    hasil_faktorial *= i

print(f"Faktorial dari {n} adalah {hasil_faktorial}")

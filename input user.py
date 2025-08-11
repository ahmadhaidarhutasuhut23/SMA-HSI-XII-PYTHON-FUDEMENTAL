# Episode input user

#data yang dimasukkan pasti string
data =input("masukkan nama: ")

print("data = ", data, ", type  =", type (data) )

# jika kita ingin mengambil int, maka
angka = float(input("masukan angka:"))
angka = int(input("masukan angka:"))
print("data = ", angka, ", type  =", type (angka) )

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))
print("data = ",biner, ", type  =", type (biner) )

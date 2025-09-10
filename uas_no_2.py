list_angka = []

print("Selesaikan isian data berikut: ")
for i in range(5):
    angka = float(input("angka ke-" + str(i + 1)+":"))
    list_angka.append(angka)

tambah_angka_1 = float(input("Masukkan angka baru: "))
tambah_angka_2 = float(input("Masukkan angka baru: "))
list_angka.append(tambah_angka_1)
list_angka.append(tambah_angka_2)

list_angka[0] = 100

angka_tuple = tuple(list_angka)
print("Tuple menghasilkan: ", angka_tuple)
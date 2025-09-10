#Input Data Mahasiswa
nim = int(input("Masukkan NIM  : "))
nama = input("Masukkan Nama : ")
jurusan = input("Masukkan Kode Jurusan (SI/SIA): ")

#Proses Perhitungan Biaya
if jurusan == "SI":
  nama_prodi = "Sistem Informasi"
  harga = 2400000
elif jurusan == "SIA":
  nama_prodi = "Sistem Informasi Akuntansi"
  harga = 2000000
else:
  print("Kode Jurusan tidak valid")
  exit()

#Input Jumlah Bayar
jumlah = int(input("Masukkan Jumlah Bayar: "))

#Proses Potongan
if jumlah >= 3000000:
  potongan = (jumlah - harga) 
else:
  potongan = 0

#Hitung Total Bayar
total = (jumlah - harga)

#Cetak Hasil
print("--------------------------------------")
print("PENDAFTARAN MAHASISWA BARU")
print("--------------------------------------")
print("NIM         :", nim)
print("Nama        :", nama)
print("Jurusan     :", nama_prodi)
print("Biaya Kuliah:", harga)
print("--------------------------------------")
print("Jumlah Bayar:", jumlah)
print("Potongan:", potongan)
print("Total Bayar:", total)
print("--------------------------------------")

#Hitung Uang Kembali
uang_kembali = jumlah - total

#Tampilkan Uang Kembali
if uang_kembali > 0:
  print("Uang Kembali:", uang_kembali)
else:
  print("Uang Anda Kurang!")
#pemrograman dasar 15 november

nama_calon_mahasiswa= input("Nama Calon Mahasiswa    : ")
nis= input("NIS                     : ")
kode_jurusan= input("Jurusan [SI/SIA]        : ")

#print
if kode_jurusan=="SI":
   nama_prodi="Sistem Informasi"
   harga=2400000
elif kode_jurusan=="SIA":
     nama_prodi="Sistem Informasi Akuntansi"
     harga= 2000000

#input jumlah pembelian
jumlah=int(input("Masukkan jumlah beli    : "))

total=(jumlah*harga)

#cetak hasil
print("----------------------------------------")
print("          PEMBAYARAN UKT                ")
print("----------------------------------------")
print("Nama Calon Mahasiswa : " +str(nama_calon_mahasiswa))
print("NIS                  : " +str(nis))
print("Kode Jurusan         : " +str(kode_jurusan))
print("Nama Prodi           : " +str(nama_prodi))
print("Harga                : " +str(harga))
print("Jumlah Beli          : " +str(jumlah))
print("----------------------------------------")
print("Total pembayaran    : " +str(total))
uang_bayar=int(input ("Masukkan Uang Bayar : "))
uang_kembali=uang_bayar-total
print("Uang kembali        : " +str(uang_kembali))

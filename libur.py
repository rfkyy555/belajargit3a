print("======================================================")
print("=================Toko Diamond MLBB====================")
print("======================================================")

nama_pembeli = input("Nama Pembeli : ")
kode_diamond = input("Kode diamond : ")
harga_diamond = int(input("Harga Diamond : "))
jumlah_diamond = int(input("Jumlah Diamond : "))

print("======================================================")
print("\hasil cetak pembelian diamond")
print("Nama pembeli           : " + str(nama_pembeli))
print("Kode Diamond           : " + str(kode_diamond))
print("Harga Diamond          : " + str(harga_diamond))
print("Jumlah Diamond         : " + str(jumlah_diamond))
c = harga_diamond * jumlah_diamond 
print("Total                  :"  , c)


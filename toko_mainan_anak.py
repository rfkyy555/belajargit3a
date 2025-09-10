print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('                    Toko Mainan Anak                   ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

nama_pembeli = input("Nama pembeli                : ")
kode_mainan = input("Masukkan kode mainan        : ")
masukkan_harga = int(input("Masukkan harga barang       : "))
jumlah_barang = int(input("Masukkan jumlah barang      : "))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\Hasil cetak pembelian barang")
print("Nama pembeli           : " + str(nama_pembeli))
print("Masukkan kode mainan   : " + str(kode_mainan))
print("Masukkan harga barang  : " + str(masukkan_harga))
print("Masukkan jumlah barang : " + str(jumlah_barang))
c = masukkan_harga * jumlah_barang 
print("Total                  :"  , c)
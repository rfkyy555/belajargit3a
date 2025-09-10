import pandas as pd
#variable yg berulang menggunakan List/matriks
list_nama_pembeli = []
list_kode_produk = []
list_nama_produk = []
list_harga_beli_produk = []
list_harga_jual_produk = []
list_jumlah_terjual = []
list_keuntungan = []

ulang=4
for i in range(ulang):
    print("Data Ke " + str(i + 1))
    list_nama_pembeli.append(input("Nama Pembeli: "))
    list_kode_produk.append(input("Kode Produk: "))
    list_nama_produk.append(input("Nama Produk: "))
    list_harga_beli_produk.append(int(input("Harga Beli Produk: ")))
    list_harga_jual_produk.append(int(input("Harga Jual Produk: ")))
    list_jumlah_terjual.append(int(input("Jumlah Terjual: ")))

#proses
for i in range(ulang):
    keuntungan_per_produk = (list_harga_jual_produk[i] - list_harga_beli_produk[i]) * list_jumlah_terjual[i]
    list_keuntungan.append(keuntungan_per_produk)
data_penjualan = {
    "Nama Pembeli"     : list_nama_pembeli,
    "Kode Produk"      : list_kode_produk,
    "Nama Produk"      : list_nama_produk,
    "Harga Beli Produk": list_harga_beli_produk,
    "Harga Jual Produk": list_harga_jual_produk,
    "Jumlah Terjual"   : list_jumlah_terjual,
    "Keuntungan"       : list_keuntungan
}
df_penjualan = pd.DataFrame(data_penjualan)
#cetak
print("======================================================== Laporan Penjualan Produk ========================================================")
print(df_penjualan)
print("==========================================================================================================================================")
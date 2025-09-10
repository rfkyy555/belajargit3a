# Input Data Mahasiswa
nim = []
nama = []
nilai = []
keterangan = []

ulang = 2
for i in range(ulang):
    print("Data ke-" + str(i + 1))
    nim.append(input("NIM: "))
    nama.append(input("Nama: "))
    nilai_mahasiswa = int(input("Nilai: ")) 
    nilai.append(nilai_mahasiswa)
    
    # Proses Perhitungan Nilai
    if nilai_mahasiswa >= 60:
        keterangan.append("Selamat, Anda Lulus!")
    else: 
        keterangan.append("Maaf, Anda Tidak Lulus")

# Cetak Hasil
print("--------------------------------------")
print("NILAI RAPORT KELULUSAN")
print("--------------------------------------")
for i in range(ulang):
    print("Data ke-" + str(i + 1))
    print("NIM         :", nim[i])
    print("Nama        :", nama[i])
    print("Nilai       :", nilai[i])
    print("Pernyataan  :", keterangan[i])
    print("--------------------------------------")
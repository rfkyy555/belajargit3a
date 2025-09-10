# Parent Class
class Pegawai:
    def __init__(self, nama, nip, gaji):
        self.nama = nama
        self.nip = nip
        self.__gaji = gaji  

    def get_gaji(self):
        return self.__gaji

    def set_gaji(self, gaji_baru):
        if isinstance(gaji_baru, (int, float)) and gaji_baru > 0:
            self.__gaji = gaji_baru
        else:
            print("Gaji harus berupa angka positif!")

    def tampilkan_info(self):
        print(f"Pegawai: {self.nama} (NIP: {self.nip})")

class Manager(Pegawai):
    def __init__(self, nama, nip, gaji, departemen):
        super().__init__(nama, nip, gaji)
        self.departemen = departemen

    def tampilkan_info(self):
        print(f"Manager: {self.nama} - Departemen: {self.departemen} - Gaji: {self.get_gaji()}")

class Developer(Pegawai):
    def __init__(self, nama, nip, gaji, bahasa):
        super().__init__(nama, nip, gaji)
        self.bahasa = bahasa

    def tampilkan_info(self):
        print(f"Developer: {self.nama} - Bahasa: {self.bahasa} - Gaji: {self.get_gaji()}")

def cetak_info_pegawai(pegawai):
    pegawai.tampilkan_info()

# Membuat objek Manager dan Developer
m1 = Manager("Andi", "M001", 15000000, "Keuangan")
d1 = Developer("Budi", "D001", 10000000, "Python")

# Menampilkan semua informasi pegawai
daftar_pegawai = [m1, d1]
for pegawai in daftar_pegawai:
    cetak_info_pegawai(pegawai)

# Update gaji developer
print("\nUpdate Gaji Developer...")
d1.set_gaji(12000000)
d1.tampilkan_info()  

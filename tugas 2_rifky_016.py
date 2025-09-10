class Person:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Alamat: {self.alamat}")

class Mahasiswa(Person):
    def __init__(self, nama, alamat, nim, prodi):
        super().__init__(nama, alamat)
        self.__nim = nim
        self.__prodi = prodi

    def get_nim(self):
        return self.__nim

    def get_prodi(self):
        return self.__prodi

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"NIM: {self.__nim}")
        print(f"Program Studi: {self.__prodi}")

class Dosen:
    def __init__(self, nama, keahlian):
        self.nama = nama
        self.keahlian = keahlian

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Keahlian: {self.keahlian}")

class MataKuliah:
    def __init__(self, nama_matkul, dosen_pengampu):
        self.nama_matkul = nama_matkul
        self.dosen_pengampu = dosen_pengampu

    def tampilkan_info(self):
        print(f"Nama MK: {self.nama_matkul}")
        print(f"Dosen Pengampu: {self.dosen_pengampu.nama}")

class Kelas:
    def __init__(self, nama_kelas, matakuliah):
        self.nama_kelas = nama_kelas
        self.matakuliah = matakuliah
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_info(self):
        print(f"Kelas: {self.nama_kelas}")
        self.matakuliah.tampilkan_info()
        print("Daftar Mahasiswa:")
        for mhs in self.daftar_mahasiswa:
            print(f"- {mhs.nama} ({mhs.get_nim()})")

class Nilai:
    def __init__(self, mahasiswa, matakuliah, nilai):
        self.mahasiswa = mahasiswa
        self.matakuliah = matakuliah
        self.__nilai = nilai

    def tampilkan_nilai(self):
        print(f"{self.mahasiswa.nama} - {self.matakuliah.nama_matkul}: {self.__nilai}")

# ======================
# Main Program
# ======================

# Objek dosen
dosen1 = Dosen("Ahmad Rois Syujak M.Kom", "Pemrograman")

# Objek Mahasiswa
mhs1 = Mahasiswa("rifky", "Bogor", "43050240016", "Teknologi Informasi")
mhs2 = Mahasiswa("pratama", "Depok", "43050240099", "Teknologi Informasi")

# Objek MataKuliah 
matkul1 = MataKuliah("Pemrograman Berorientasi Objek", dosen1)

# Objek Kelas
kelasA = Kelas("Kelas A", matkul1)
kelasA.tambah_mahasiswa(mhs1)
kelasA.tambah_mahasiswa(mhs2)

# Objek Nilai
nilai1 = Nilai(mhs1, matkul1, 90)
nilai2 = Nilai(mhs2, matkul1, 85)

# Output
print("\n=== Informasi Dosen ===")
dosen1.tampilkan_info()

print("\n=== Informasi Mahasiswa ===")
mhs1.tampilkan_info()
print()
mhs2.tampilkan_info()

print("\n=== Informasi Mata Kuliah ===")
matkul1.tampilkan_info()

print("\n=== Informasi Kelas ===")
kelasA.tampilkan_info()

print("\n=== Informasi Nilai ===")
nilai1.tampilkan_nilai()
nilai2.tampilkan_nilai()

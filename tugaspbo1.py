#kelas mahasiswa

class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def perkenalan(self):
        print(f"Hallo, nama saya {self.nama} dengan NIM {self.nim} dari prodi {self.prodi}")


# Membuat objek dari class Mahasiswa
mhs1 = Mahasiswa("Arul", "22021001", "Teknologi Informasi")
mhs2 = Mahasiswa("Apoy", "23782263", "Psikologi Islam")

#metode perkenalan

mhs1.perkenalan()

print("========================================================================")

mhs2.perkenalan()

print("========================================================================")
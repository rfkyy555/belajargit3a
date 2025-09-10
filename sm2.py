class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def perkenalan(self):
        print(f"Hallo, nama saya {self.nama} dengan NIM {self.nim}")

# Membuat objek dari class Mahasiswa
mhs1 = Mahasiswa("Rina", "22021001")
mhs1.perkenalan()

#Membuat class dan object

class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat, nohp, email):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat
        self.nohp = nohp
        self.email = email

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}, Nim saya {self.nim}, dari prodi {self.prodi}, alamat saya di {self.alamat}, nomor hp saya {self.nohp}, dan email saya {self.email} salam kenal!")

#objeknya
mhs = Mahasiswa("Rifky Surya Pratama", 43050240016, "Teknologi Informasi", "Pulutan", 6287783746204, "rifkysurya@gmail.com")

mhs.perkenalan()
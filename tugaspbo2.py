#kelas kendaraan

class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        print(f"Merk kendaraan : {self.merk}")
        print(f"Tahun kendaraan : {self.tahun}")

class Mobil(Kendaraan):
    def __init__(self, merk, tahun, tipe,):
        super().__init__(merk, tahun)
        self.tipe = tipe

    def info(self):
        print(f"Mobil {self.merk} dengan tipe {self.tipe} Tahun {self.tahun}")


# Membuat objek dari class Mobil
mobil1 = Mobil("Toyota", "2020", "SUV")
mobil1.info()
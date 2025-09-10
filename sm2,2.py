class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print(f"Merk kendaraan: {self.merk}")

class Mobil(Kendaraan):
    def __init__(self, merk, tipe):
        super().__init__(merk)
        self.tipe = tipe

    def info(self):
        print(f"Mobil {self.merk} dengan tipe {self.tipe}")

# Membuat objek
mobil1 = Mobil("Toyota", "SUV")
mobil1.info()


# Kelas induk
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
        self.__biaya_servis = 0  

    def get_biaya_servis(self):
        return self.__biaya_servis

    def set_biaya_servis(self, biaya):
        if biaya >= 0:
            self.__biaya_servis = biaya
        else:
            print("Biaya tidak valid.")

    def servis(self):  
        print("Servis umum kendaraan")

# Subclass untuk Motor
class Motor(Kendaraan):
    def __init__(self, merek, tahun, tipe_motor):
        super().__init__(merek, tahun)  
        self.tipe_motor = tipe_motor

    def servis(self):  
        self.set_biaya_servis(100_000)  
        print(f"Servis motor {self.merek} ({self.tipe_motor})")
        print(f"Biaya servis: Rp{self.get_biaya_servis():,}")

# Subclass untuk Mobil
class Mobil(Kendaraan):
    def __init__(self, merek, tahun, tipe_mobil):
        super().__init__(merek, tahun)
        self.tipe_mobil = tipe_mobil

    def servis(self):  
        self.set_biaya_servis(300_000)  
        print(f"Servis mobil {self.merek} ({self.tipe_mobil})")
        print(f"Biaya servis: Rp{self.get_biaya_servis():,}")

# Main program
if __name__ == "__main__":
    # Membuat daftar kendaraan
    daftar_kendaraan = [
        Motor("Honda", 2020, "Bebek"),
        Mobil("Toyota", 2018, "SUV"),
        Motor("Yamaha", 2022, "Sport")
    ]

# Polimorfisme dalam aksi
    for kendaraan in daftar_kendaraan:
        kendaraan.servis()
        print("==============================")
        print("==============================")
# class Anjing
class Anjing:
    def bersuara(self):
        print("Anjing menggonggong")

# class Kucing
class Kucing:
    def bersuara(self):
        print("Kucing meong")

# fungsi yang menerima objek dan memanggil method bersuara()
def suara_hewan(hewan):
    hewan.bersuara()

# membuat objek dari class Anjing dan Kucing
anjing = Anjing()
kucing = Kucing()

# memanggil fungsi suara_hewan untuk kedua objek
suara_hewan(anjing)   
suara_hewan(kucing)
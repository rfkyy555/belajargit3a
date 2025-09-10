class BankAccount:
    def __init__(self, nama, saldo):
        self.nama = nama       # Public Attribute
        self.__saldo = saldo   # Private Attribute

    def lihat_saldo(self):
        print(f"Saldo {self.nama}: Rp {self.__saldo}")

    def tarik_tunai(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil menarik Rp {jumlah}")
        else:
            print("Saldo tidak mencukupi!")

    def saldo_sekarang(self):
        print(f"Sisa Saldo {self.nama}: Rp {self.__saldo}")
        

# Membuat objek
akun1 = BankAccount("Andi", 500000)
akun1.lihat_saldo()
akun1.tarik_tunai(200000)
akun1.saldo_sekarang()
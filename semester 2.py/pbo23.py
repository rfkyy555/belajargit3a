class Anggota:
    def _init_(self, nama, id_anggota):
        self.__nama = nama
        self.__id_anggota = id_anggota
        self.__daftar_pinjaman = []
    
    def get_nama(self):
        return self.__nama
    
    def get_id(self):
        return self.__id_anggota
    
    def tambah_pinjaman(self, buku):
        self.__daftar_pinjaman.append(buku)
    
    def info(self):
        return f"{self._nama} ({self._id_anggota})"

class Mahasiswa(Anggota):
    def _init_(self, nama, id_anggota, nim):
        super()._init_(nama, id_anggota)
        self.__nim = nim
        self.__batas_pinjam = 3
    
    def get_batas_pinjam(self):
        return self.__batas_pinjam

class Dosen(Anggota):
    def _init_(self, nama, id_anggota, nip):
        super()._init_(nama, id_anggota)
        self.__nip = nip
        self.__batas_pinjam = 5
    
    def get_batas_pinjam(self):
        return self.__batas_pinjam

class Buku:
    def _init_(self, judul, pengarang, isbn):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__isbn = isbn
        self.__tersedia = True
    
    def get_judul(self):
        return self.__judul
    
    def get_isbn(self):
        return self.__isbn
    
    def is_tersedia(self):
        return self.__tersedia
    
    def pinjam(self):
        self.__tersedia = False
    
    def kembalikan(self):
        self.__tersedia = True

class Peminjaman:
    def _init_(self, anggota, buku, tanggal):
        self.__anggota = anggota
        self.__buku = buku
        self.__tanggal = tanggal
    
    def info(self):
        return f"{self._anggota.get_nama()} pinjam {self.buku.get_judul()} ({self._tanggal})"

class SistemPerpustakaan:
    def _init_(self):
        self.__anggota = []
        self.__buku = []
        self.__peminjaman = []
    
    def tambah_anggota(self, anggota):
        self.__anggota.append(anggota)
    
    def tambah_buku(self, buku):
        self.__buku.append(buku)
    
    def pinjam_buku(self, id_anggota, isbn, tanggal):
        anggota = next((a for a in self.__anggota if a.get_id() == id_anggota), None)
        buku = next((b for b in self.__buku if b.get_isbn() == isbn), None)
        
        if anggota and buku and buku.is_tersedia():
            buku.pinjam()
            anggota.tambah_pinjaman(buku)
            peminjaman = Peminjaman(anggota, buku, tanggal)
            self.__peminjaman.append(peminjaman)
            print(f"Berhasil: {peminjaman.info()}")
        else:
            print("Gagal meminjam!")
    
    def kembalikan_buku(self, isbn):
        buku = next((b for b in self.__buku if b.get_isbn() == isbn), None)
        if buku:
            buku.kembalikan()
            print(f"Buku {buku.get_judul()} dikembalikan")

# Contoh penggunaan
perpus = SistemPerpustakaan()

# Anggota Kelompok 1 Kelas A
rifky = Mahasiswa("Rifky Surya Pratama", "016", "2023016")
zulfikar = Mahasiswa("Muhammad Zulfikar Said Kamil", "015", "2023015")
naufal = Mahasiswa("Achmad Naufal Arifin", "028", "2023028")
zaky = Mahasiswa("Zaky Mahya", "020", "2023020")

perpus.tambah_anggota(rifky)
perpus.tambah_anggota(zulfikar)
perpus.tambah_anggota(naufal)
perpus.tambah_anggota(zaky)

# Buku
buku1 = Buku("Python Programming", "Guido", "001")
buku2 = Buku("Data Structure", "Cormen", "002")

perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

# Test peminjaman
perpus.pinjam_buku("016", "001", "2025-06-01")
perpus.pinjam_buku("015", "002", "2025-06-01")
perpus.kembalikan_buku("001")
from datetime import datetime
from tabulate import tabulate

class Buku:
    def __init__(self, judul, pengarang, isbn, tahun, stok):
        self.judul = judul
        self.pengarang = pengarang
        self.isbn = isbn
        self.tahun = tahun
        self.stok = stok
        self.dipinjam = 0

    def pinjam(self):
        if self.stok > 0:
            self.stok -= 1
            self.dipinjam += 1
            return True
        return False

    def kembali(self):
        if self.dipinjam > 0:
            self.stok += 1
            self.dipinjam -= 1
            return True
        return False

class Anggota:
    def __init__(self, nama, id_anggota, email):
        self.nama = nama
        self.id = id_anggota
        self.email = email
        self.pinjam = []
        self.maks_pinjam = 3

    def pinjam_buku(self, buku):
        if len(self.pinjam) < self.maks_pinjam and buku.pinjam():
            self.pinjam.append(buku)
            return True
        return False

    def kembali_buku(self, buku):
        if buku in self.pinjam and buku.kembali():
            self.pinjam.remove(buku)
            return True
        return False

class Mahasiswa(Anggota):
    def __init__(self, nama, id_anggota, email, nim, jurusan):
        super().__init__(nama, id_anggota, email)
        self.nim = nim
        self.jurusan = jurusan
        self.maks_pinjam = 5

class Dosen(Anggota):
    def __init__(self, nama, id_anggota, email, nip, fakultas):
        super().__init__(nama, id_anggota, email)
        self.nip = nip
        self.fakultas = fakultas
        self.maks_pinjam = 10

class Peminjaman:
    def __init__(self, id_pinjam, anggota, buku, tgl_pinjam):
        self.id = id_pinjam
        self.anggota = anggota
        self.buku = buku
        self.tgl_pinjam = tgl_pinjam
        self.tgl_kembali = None
        self.status = "Dipinjam"

    def kembalikan(self, tgl_kembali):
        self.tgl_kembali = tgl_kembali
        self.status = "Dikembalikan"

class SistemPerpustakaan:
    def __init__(self):
        self.buku = []
        self.anggota = []
        self.peminjaman = []
        self.next_id = 1

    def tambah_buku(self, b): self.buku.append(b)
    def tambah_anggota(self, a): self.anggota.append(a)

    def cari_buku(self, judul):
        return next((b for b in self.buku if judul.lower() in b.judul.lower()), None)

    def cari_anggota(self, id):
        return next((a for a in self.anggota if a.id == id), None)

    def pinjam_buku(self, id_anggota, judul_buku, tgl):
        anggota = self.cari_anggota(id_anggota)
        buku = self.cari_buku(judul_buku)
        if anggota and buku and anggota.pinjam_buku(buku):
            p = Peminjaman(self.next_id, anggota, buku, tgl)
            self.peminjaman.append(p)
            self.next_id += 1
            print(f"{anggota.nama} meminjam '{buku.judul}'")
        else:
            print("Peminjaman gagal.")

    def kembali_buku(self, id_anggota, judul_buku, tgl):
        anggota = self.cari_anggota(id_anggota)
        buku = self.cari_buku(judul_buku)
        if anggota and buku and anggota.kembali_buku(buku):
            for p in self.peminjaman:
                if p.anggota == anggota and p.buku == buku and p.status == "Dipinjam":
                    p.kembalikan(tgl)
                    print(f"{anggota.nama} mengembalikan '{buku.judul}'")
                    return
        else:
            print("Pengembalian gagal.")

    def tampilkan(self):
        print("\n=== DAFTAR BUKU ===")
        buku_data = [[b.judul, b.pengarang, b.isbn, b.tahun, b.stok, b.dipinjam] for b in self.buku]
        print(tabulate(buku_data, headers=["Judul", "Pengarang", "ISBN", "Tahun", "Stok", "Dipinjam"], tablefmt="grid"))

        print("\n=== DAFTAR ANGGOTA ===")
        anggota_data = [[a.nama, a.id, a.email, len(a.pinjam), a.maks_pinjam] for a in self.anggota]
        print(tabulate(anggota_data, headers=["Nama", "ID", "Email", "Jumlah Pinjam", "Batas Pinjam"], tablefmt="grid"))

        print("\n=== PEMINJAMAN AKTIF ===")
        pinjam_data = [[p.id, p.anggota.nama, p.buku.judul, p.tgl_pinjam, p.status]
                       for p in self.peminjaman if p.status == "Dipinjam"]
        print(tabulate(pinjam_data, headers=["ID Peminjaman", "Nama Anggota", "Judul Buku", "Tanggal Pinjam", "Status"], tablefmt="grid"))

def main():
    s = SistemPerpustakaan()

    # Tambah buku
    s.tambah_buku(Buku("Pemrograman Python", "John Doe", "123", 2023, 5))
    s.tambah_buku(Buku("Struktur Data", "Jane Smith", "456", 2022, 3))
    s.tambah_buku(Buku("Database Systems", "Bob Johnson", "789", 2021, 4))

    # Tambah mahasiswa
    mahasiswa = [
        Mahasiswa("Rifky", "016", "rifky@em", "016", "TI"),
        Mahasiswa("Zulfikar", "015", "zul@em", "015", "TI"),
        Mahasiswa("Said", "017", "said@em", "017", "TI"),
        Mahasiswa("Naufal", "028", "naufal@em", "028", "TI"),
        Mahasiswa("Zaky", "020", "zaky@em", "020", "TI"),
    ]
    for m in mahasiswa:
        s.tambah_anggota(m)

    # Tambah dosen
    s.tambah_anggota(Dosen("Ahmad", "D001", "ahmad@univ", "999", "Teknik"))

    # Simulasi peminjaman
    s.pinjam_buku("016", "Pemrograman Python", "2025-06-01")
    s.pinjam_buku("015", "Struktur Data", "2025-06-01")
    s.pinjam_buku("D001", "Database Systems", "2025-06-01")

    # Tampilkan data
    s.tampilkan()

    # Simulasi pengembalian
    print("\n=== PENGEMBALIAN ===")
    s.kembali_buku("016", "Pemrograman Python", "2025-06-08")

    # Tampilkan data lagi
    s.tampilkan()

if __name__ == "__main__":
    main()
    
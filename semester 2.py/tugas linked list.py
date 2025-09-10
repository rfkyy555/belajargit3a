# Mendefinisikan kelas Node
class Node:
    def __init__(self, data):  # Perbaikan: seharusnya __init__, bukan _init_
        self.data = data       # Menyimpan data
        self.next = None       # Pointer ke node berikutnya


# Mendefinisikan kelas LinkedList
class LinkedList:
    def __init__(self):  # Perbaikan: __init__ (dua underscore)
        self.head = None

# Menambahkan node di awal linked list
    def tambah_awal(self, data):
        new_node = Node(data)    # Buat node baru
        new_node.next = self.head  # Hubungkan node baru ke head sekarang
        self.head = new_node       # Perbarui head ke node baru

# Menambahkan node di akhir linked list
    def tambah_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:     # Cari node terakhir
            last_node = last_node.next
        last_node.next = new_node  # Tambahkan node baru di akhir

# Menghapus node dari awal
    def hapus_awal(self):
        if self.head is None:
            print("List kosong")
            return
        self.head = self.head.next  # Hapus node pertama dengan memindahkan head

# Menghapus node dari akhir
    def hapus_akhir(self):
        if self.head is None:
            print("List kosong")
            return
        if self.head.next is None:  # Jika hanya ada satu node
            self.head = None
            return

        temp = self.head
        while temp.next.next:  # Temukan node sebelum terakhir
            temp = temp.next
        temp.next = None       # Putuskan link ke node terakhir

# Menampilkan isi linked list
    def tampil(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None\n")


# ====== PROGRAM UTAMA ======

if __name__ == '__main__':  # Perbaikan: __name__ dan __main__ harus dua underscore
    llist = LinkedList()

# Memasukkan beberapa kata di depan linked list
    llist.tambah_awal('got')
    llist.tambah_awal('tikus')
    llist.tambah_awal('mengejar')
    llist.tambah_awal('kucing')

# Memasukkan kata di akhir linked list
    llist.tambah_akhir('besar')

# Menampilkan list sebelum penghapusan
    print("List sebelum hapus:")
    llist.tampil()

# Menghapus node dari awal dan akhir
    llist.hapus_awal()
    llist.hapus_akhir()

# Menampilkan list setelah penghapusan
    print("List setelah hapus:")
    llist.tampil()

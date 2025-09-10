# Mendefinisikan kelas Node
class Node:
    def __init__(self, data):
        self.data = data       # Menyimpan data
        self.next = None       # Pointer ke node berikutnya

# Mendefinisikan kelas LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di awal linked list
    def tambah_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Menambahkan node di akhir linked list
    def tambah_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Menambahkan node di tengah pada posisi tertentu
    def tambah_tengah(self, data, posisi):
        if posisi <= 0:
            print("Posisi harus >= 1 (gunakan tambah_awal jika ingin di awal)")
            return

        new_node = Node(data)

        if posisi == 1:
            self.tambah_awal(data)
            return

        temp = self.head
        count = 1

        # Cari posisi sebelumnya
        while temp is not None and count < posisi - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Posisi di luar jangkauan.")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Menghapus node dari awal
    def hapus_awal(self):
        if self.head is None:
            print("List kosong")
            return
        self.head = self.head.next

    # Menghapus node dari akhir
    def hapus_akhir(self):
        if self.head is None:
            print("List kosong")
            return
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Menampilkan isi linked list
    def tampil(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None\n")


# ====== PROGRAM UTAMA ======
if __name__ == '__main__':
    llist = LinkedList()

    # Menambahkan data
    llist.tambah_awal('got')
    llist.tambah_awal('tikus')
    llist.tambah_awal('mengejar')
    llist.tambah_awal('kucing')
    llist.tambah_akhir('besar')
    llist.tambah_tengah('seekor', 3)  # Menyisipkan di posisi ke-3

    # Menampilkan sebelum penghapusan
    print("List sebelum hapus:")
    llist.tampil()

    # Menghapus node dari awal dan akhir
    llist.hapus_awal()
    llist.hapus_akhir()

    # Menampilkan setelah penghapusan
    print("List setelah hapus:")
    llist.tampil()

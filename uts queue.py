#Kasus pendaftaran mahasiswa

class Node:
    def __init__(self, data):  # Perbaikan: __init__
        self.data = data
        self.next = None

class Queue:
    def __init__(self):  # Perbaikan: __init__
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Antrian kosong"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Antrian kosong"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        print("Mahasiswa dalam antrian:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

#Pendaftaran ujian mahasiswa
pendaftaran = Queue()

#Mahasiswa A, B, C, D, E mendaftar
for mhs in ['A', 'B', 'C', 'D', 'E']:
    pendaftaran.enqueue(mhs)

#Antrian awal
pendaftaran.printQueue()

#Mahasiswa A dan B diproses
print("Berhasil diproses:", pendaftaran.dequeue())
print("Berhasil diproses:", pendaftaran.dequeue())

#Mahasiswa F dan G mendaftar
for mhs in ['F', 'G']:
    pendaftaran.enqueue(mhs)

# Hasil akhir kondisi queue setelah F dan G masuk 
pendaftaran.printQueue()

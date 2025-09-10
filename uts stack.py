# Kasus undo di aplikasi penulis (Stack)

class UndoStack:
    def __init__(self):  # Perbaikan: __init__
        self.stack = []

    def push(self, kata):
        self.stack.append(kata)
        print(f"Push: '{kata}' -> Stack: {self.stack}")

    def pop(self):
        if self.stack:
            hapus = self.stack.pop()
            print(f"Undo: '{hapus}' -> Stack: {self.stack}")
            return hapus
        else:
            print("Undo error: Tidak Ada Tumpukkan")
            return None

#Output
undo_stack = UndoStack()
undo_stack.push("Halo")
undo_stack.push("Apa kabar")
undo_stack.push("Semua")

undo_stack.pop()  
undo_stack.pop() 
undo_stack.pop()  
undo_stack.pop() 
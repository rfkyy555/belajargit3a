class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi traversal secara rekursif
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

# Membentuk struktur binary tree sesuai soal:
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.right.right = Node('E')

# Menampilkan hasil traversal dengan format rapi
print("=" * 28)
print("     Hasil Traversal Tree")
print("=" * 28)

print("Inorder   :", end=' ')
inorder(root)

print("\nPreorder  :", end=' ')
preorder(root)

print("\nPostorder :", end=' ')
postorder(root)

print("\n" + "=" * 28)

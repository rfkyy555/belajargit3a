class Node: 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.key, end="")
            self.inorder(node.right)

tree = BST()
for k in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(k)

tree.inorder(tree.root)
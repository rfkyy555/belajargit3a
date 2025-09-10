class Node:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

class Traversal:
    # root -> left -> right
    def pre_order(self, node):
        if node is None:
            return
        print(node.data, end=" -> ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    # left -> root -> right
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data, end=" -> ")
        self.in_order(node.right)

    # left -> right -> root
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=" -> ")

if __name__ == "__main__": 
    nodeR = Node("R")
    nodeA = Node("A")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeB = Node("B")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")

    # Struktur tree
    nodeR.left = nodeA
    nodeR.right = nodeB
    nodeA.left = nodeC
    nodeA.right = nodeD
    nodeB.left = nodeE
    nodeB.right = nodeF
    nodeF.left = nodeG

    traversal = Traversal()

    print("-- pre order --")
    traversal.pre_order(nodeR)
    print("None\n-----")  

    print("-- in order --")
    traversal.in_order(nodeR)
    print("None\n-----")

    print("-- post order --")
    traversal.post_order(nodeR)
    print("None")

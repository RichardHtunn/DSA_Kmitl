class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return self.root

        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = node
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    break
                current = current.right

        return self.root

    def delete(self, root, data):
        if root is None:
            print("Error! Not Found DATA")
            return None

        if root.data > data:
            root.left = self.delete(root.left, data)
        elif root.data < data:
            root.right = self.delete(root.right, data)
        elif root.data == data:
            if root.left is None and root.right is None:
                root = None
            elif root.left is not None and root.right is None:
                root = root.left
            elif root.left is None and root.right is not None:
                root = root.right
            elif root.left is not None and root.right is not None:
                temp = self.minValueNode(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, root.data)

        self.root = root
        return self.root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [x.split() for x in input('Enter Input : ').split(",")]

root = None
for key, value in inp:
    if key == "i":
        print(f"insert {value}")
        root = T.insert(int(value))
        T.printTree(root)
    if key == "d":
        print(f"delete {value}")
        root = T.delete(root, int(value))
        T.printTree(root)
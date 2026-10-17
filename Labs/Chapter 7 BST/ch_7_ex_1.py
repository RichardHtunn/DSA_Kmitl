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

        new_node = Node(data)

        # If tree is empty, first input becomes root
        if self.root is None:
            self.root = new_node
            return self.root

        current = self.root

        while True:

            # Go to left
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left

            # Go to right
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

        return self.root

    def printTree(self, node, level=0):

        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    root = T.insert(i)

T.printTree(root)
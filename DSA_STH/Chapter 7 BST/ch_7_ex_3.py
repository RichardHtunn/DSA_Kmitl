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

        if self.root is None:
            self.root = new_node
            return self.root

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

        return self.root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def countLessEqual(self, node, k):
        if node is None:
            return 0

        if node.data <= k:
            return (1 +
                    self.countLessEqual(node.left, k) +
                    self.countLessEqual(node.right, k))

        return self.countLessEqual(node.left, k)


T = BST()

inp = input('Enter Input : ')
numbers, k = inp.split('/')

numbers = [int(i) for i in numbers.split()]
k = int(k)

for i in numbers:
    root = T.insert(i)

T.printTree(root)

print('-' * 50)
print(T.countLessEqual(root, k))
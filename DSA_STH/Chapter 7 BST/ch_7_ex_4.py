class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return self.root

        current = self.root

        while True:
            if val < current.data:
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

    def delete(self, r, data):

        if r is None:
            return r

        if data < r.data:
            r.left = self.delete(r.left, data)

        elif data > r.data:
            r.right = self.delete(r.right, data)

        else:

            # no left child
            if r.left is None:
                return r.right

            # no right child
            if r.right is None:
                return r.left

            # two children:
            # find smallest node in right subtree
            temp = r.right

            while temp.left is not None:
                temp = temp.left

            r.data = temp.data
            r.right = self.delete(r.right, temp.data)

        return r


def printTree90(node, level=0):

    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()

data = input("Enter Input : ").split(",")

for command in data:

    command = command.split()

    action = command[0]
    value = int(command[1])

    if action == 'i':

        print("insert", value)

        tree.root = tree.insert(value)

        printTree90(tree.root)

    elif action == 'd':

        print("delete", value)

        # Search for the value first
        current = tree.root
        found = False

        while current is not None:

            if value == current.data:
                found = True
                break

            elif value < current.data:
                current = current.left

            else:
                current = current.right

        if found:
            tree.root = tree.delete(tree.root, value)

        else:
            print("Error! Not Found DATA")

        # print tree whether deletion succeeds or fails
        printTree90(tree.root)
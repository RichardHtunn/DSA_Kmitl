class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self.update_height(node)

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def min_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            temp = self.min_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        self.update_height(node)

        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete_root(self):
        if self.root is not None:
            self.root = self._delete(self.root, self.root.key)

    def print_tree(self):
        if self.root is None:
            return

        h = self.height(self.root)
        current = [self.root]

        for level in range(h):
            first_space = 2 ** (h - level + 1) - 1
            step = 2 ** (h - level + 2)

            line = ""
            next_level = []

            for i, node in enumerate(current):
                position = first_space + i * step

                if len(line) < position:
                    line += " " * (position - len(line))

                line += str(node.key)

                if node.left is not None:
                    next_level.append(node.left)

                if node.right is not None:
                    next_level.append(node.right)

            print(line)
            current = next_level


tree = AVLTree()

print(" *** AVL Tree ***")
numbers = list(map(int, input("Enter numbers to insert: ").split()))

for number in numbers:
    tree.insert(number)

tree.print_tree()

while tree.root is not None:
    print("------------------------------")
    tree.delete_root()

    if tree.root is not None:
        tree.print_tree()

print("===== End of program =====")
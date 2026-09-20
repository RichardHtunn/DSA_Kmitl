class AVLTree:

    class AVLNode:

        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)


    def __init__(self, root=None):
        self.root = None if root is None else root


    def add(self, data):
        data = int(data)
        self.root = AVLTree._add(self.root, data)


    def _add(root, data):

        # Normal BST insertion
        if root is None:
            return AVLTree.AVLNode(data)

        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            # Equal values also go to the right
            root.right = AVLTree._add(root.right, data)

        # Update height
        root.setHeight()

        # Check balance
        balance = root.balanceValue()

        # Left heavy
        if balance == -2:

            # Left-Right case
            if root.left.balanceValue() == 1:
                root.left = AVLTree.rotateRightChild(root.left)

            # Left-Left case
            root = AVLTree.rotateLeftChild(root)

        # Right heavy
        elif balance == 2:

            # Right-Left case
            if root.right.balanceValue() == -1:
                root.right = AVLTree.rotateLeftChild(root.right)

            # Right-Right case
            root = AVLTree.rotateRightChild(root)

        root.setHeight()

        return root


    def rotateLeftChild(root):

        newRoot = root.left

        root.left = newRoot.right
        newRoot.right = root

        # Update heights
        root.setHeight()
        newRoot.setHeight()

        return newRoot


    def rotateRightChild(root):

        newRoot = root.right

        root.right = newRoot.left
        newRoot.left = root

        # Update heights
        root.setHeight()
        newRoot.setHeight()

        return newRoot


    def postOrder(self):

        result = AVLTree._postOrder(self.root)

        print("AVLTree post-order :", end="")

        for data in result:
            print("", data, end="")

        print()


    def _postOrder(root):

        if root is None:
            return []

        result = []

        # Left
        result.extend(AVLTree._postOrder(root.left))

        # Right
        result.extend(AVLTree._postOrder(root.right))

        # Root
        result.append(root.data)

        return result


    def printTree(self):
        AVLTree._printTree(self.root)
        print()


    def _printTree(node, level=0):

        if node is not None:
            AVLTree._printTree(node.right, level + 1)

            print('     ' * level, node.data)

            AVLTree._printTree(node.left, level + 1)


avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":
        avl1.add(i[3:])

    elif i[:2] == "PR":
        avl1.printTree()

    elif i[:2] == "PO":
        avl1.postOrder()
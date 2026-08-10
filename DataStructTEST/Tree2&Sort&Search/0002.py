class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVLTree:
    def __init__(self):
        self.root = None

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder1(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def print_inorder(self, node, first = True):
        if first == True:
            print("in_order  --> ", end='')
            first = False
        if node != None:
            self.print_inorder(node.left, first)
            print(node.data, end=' ')
            self.print_inorder(node.right, first)

    def print_postorder(self, node, first =True):
        if first == True:
            print("postorder --> ", end='')
            first = False
        if node != None:
            self.print_postorder(node.left, first)
            self.print_postorder(node.right, first)
            print(node.data, end=' ')

    def print_preorder(self, node, first = True):
        if first == True:
            print("preorder  --> ", end='')
            first = False
        if node != None:
            print(node.data, end=' ')
            self.print_preorder(node.left, first)
            self.print_preorder(node.right, first)

    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Return the new root
        return y

    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y

    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)

        if balance < -1 and key >= root.right.data:
            return self.leftRotate(root)

        if balance > 1 and key >= root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


print(" *** AVL Tree ***")

input_string = input("Enter some numbers : ")

bst = AVLTree()
root = None

for n in input_string.split():
    root = bst.insert(root, int(n))

bst.print_inorder(root, True)
print("")
bst.print_preorder(root, True)
print("")
bst.print_postorder(root, True)
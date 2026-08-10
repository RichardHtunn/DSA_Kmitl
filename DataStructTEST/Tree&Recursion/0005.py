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
        # Code Here
        if self.root is None:
            self.root = Node(data)
            return self.root
        temp = self.root
        while True:
            if temp.data <= data:
                if temp.right is None:
                    temp.right = Node(data)
                    break
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                else:
                    temp = temp.left
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print(node.data, end=' ')
            self.inOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=' ')

    def preOrder(self, node):
        if node != None:
            print(node.data, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def Breadth(self, root):
        if root is None:
            return
        
        queue = []
        queue.append(root)

        while len(queue) > 0:
            print(queue[0].data, end=' ')
            node = queue.pop(0)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)


print(" *** Binary Search Tree ***")

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

print("")
print(" --- Tree traversal ---")

print("Level order : ", end='')
T.Breadth(root)
print("")

print("Preorder : ", end='')
T.preOrder(root)
print("")

print("Inorder : ", end='')
T.inOrder(root)
print("")

print("Postorder : ", end='')
T.postOrder(root)
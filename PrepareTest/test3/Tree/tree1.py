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
            if temp.data < data:
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

    def checkLessThan(self, node, number, q=[]):
        if node != None:
            self.checkLessThan(node.left, number, q)
            if node.data < number:
                q.append(node.data)
            self.checkLessThan(node.right, number, q)
        
        return q

    def checkMoreThan(self, node, k):
        if node != None:
            self.checkMoreThan(node.left, k)
            if node.data > k:
                node.data = node.data*3
            self.checkMoreThan(node.right, k)
        return

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

    def expressionTree(self, text):
        operator = ['+', '-', '*', '/']
        s = []

        for i in range(0, len(text), 1):
            if text[i] in operator:
                operator_Node = Node(text[i])
                operator_Node.right = s.pop()
                operator_Node.left = s.pop()
                s.append(operator_Node)
            else:
                operand_Node = Node(text[i])
                s.append(operand_Node)
        return s.pop()

    def infix(self, node):
        if node != None:
            if node.left is None and node.right is None:
                pass
            else:
                print("(", end='')
            self.infix(node.left)
            print(node.data, end='')
            self.infix(node.right)
            if node.left is None and node.right is None:
                pass
            else:
                print(")", end='')

    def prefix(self, node):
        if node != None:
            print(node.data, end='')
            self.prefix(node.left)
            self.prefix(node.right)

    def minValueNode(self, node):
        current = node

        while current.left != None:
            current = current.left
        
        return current

    def Search(self, data):
        temp = self.root
        while temp:
            if temp.data < data:
                temp = temp.left
            elif temp.data > data:
                temp = temp.right
            else:
                return True
        return False
            

    def deleteNode(self, node, key):
        
        # if self.Search(self.root) is False:
        #     print("Error! Not Found DATA")
        #     return
        
        if node is None:
            print("Error! Not Found DATA")
            return None
        
        if key < node.data:
            node.left = self.deleteNode(node.left, key)
        elif key > node.data:
            node.right = self.deleteNode(node.right, key)
        elif key == node.data:
            if node.left == None and node.right == None:
                node = None
            elif node.left != None and node.right == None:
                node = node.left
            elif node.left == None and node.right != None:
                node = node.right
            elif node.left != None and node.right != None:
                temp = self.minValueNode(node.right)
                node.data = temp.data
                node.right = self.deleteNode(node.right, node.data)

        
        self.root = node
        
        return self.root


T = BST()

inp = [i.split() for i in input('Enter Input : ').split(",")]
print(inp)
for i in range(len(inp)):
    if inp[i][0] == 'i':
        print("insert", inp[i][1])
        temp = T.insert(int(inp[i][1]))
        T.printTree(T.root)
    elif inp[i][0] == 'd':
        print("delete", inp[i][1])
        temp = T.deleteNode(temp, int(inp[i][1]))
        T.printTree(temp)
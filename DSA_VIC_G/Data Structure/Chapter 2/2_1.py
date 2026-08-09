class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree():
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, node):
        new_root = node.left
        temp = new_root.right
        new_root.right = node
        node.left = temp
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def left_rotate(self, node):
        new_root = node.right
        temp = new_root.left
        new_root.left = node
        node.right = temp
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def insert(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Case 2: Left-Left  
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Case 2: Right-Right  
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Case 3: Left-Right 
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4: Right-Left 
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node  

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)      

    def delete(self, node, value):
        if not node:
            return node
        
        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)           
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.get_min_value_node(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)
        
        if node is None:
            return node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Case 1: Left-Left 
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Case 2: Left-Right 
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 3: Right-Right 
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Case 4: Right-Left 
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ") 
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ") 
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('    ' * level + str(node.value))
            self.print_tree(node.left, level + 1)

my_tree = AVL_Tree()
root = None
User_input = input("Enter commands: ").split(",")


for i in User_input:
    if i.startswith("i "):
        parts = i.split(" ")
        number = int(parts[1])
        root = my_tree.insert(root, number)

    elif i.startswith("d "):
        parts = i.split(" ")
        number = int(parts[1])
        root = my_tree.delete(root, number)

    elif i == "in":
        print("Inorder: ", end="")
        my_tree.inorder(root)
        print()

    elif i == "print":
        print("Tree structure:")
        my_tree.print_tree(root, 0)

    elif i == "pre":
        print("Preorder: ", end="")
        my_tree.preorder(root)
        print() 

    elif i == "post":
        print("Postorder: ", end="")
        my_tree.postorder(root)
        print()















class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def createExpressionTree(postfix):
    stack = []
    operators = "+-*/"

    for ch in postfix:

        # Operand
        if ch not in operators:
            stack.append(Node(ch))

        # Operator
        else:
            new_node = Node(ch)

            # IMPORTANT: first pop = right child
            new_node.right = stack.pop()
            new_node.left = stack.pop()

            stack.append(new_node)

    return stack.pop()


def infix(node):
    if node.left is None and node.right is None:
        return str(node.data)

    return "(" + infix(node.left) + str(node.data) + infix(node.right) + ")"


def prefix(node):
    if node is None:
        return ""

    return str(node.data) + prefix(node.left) + prefix(node.right)


postfix = input("Enter Postfix : ")

root = createExpressionTree(postfix)

print("Tree :")
printTree90(root)

print("-" * 50)

print("Infix :", infix(root))
print("Prefix :", prefix(root))
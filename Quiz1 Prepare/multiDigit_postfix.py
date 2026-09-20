class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop() if self.items else None
        
    def size(self):
        return len(self.items)

def evaluate_advanced_postfix(expression):
    stack = Stack()
    tokens = expression.split()
    
    for token in tokens:
        # Check if token is a number (including negatives like -15)
        if token.lstrip('-').isdigit():
            stack.push(int(token))
        else:
            # Need at least two operands for these operations
            if stack.size() < 2:
                return "ERR: SYNTAX"
                
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                if b == 0:
                    return "ERR: DIV/0"
                stack.push(int(a / b)) # Integer division
            elif token == '^':
                stack.push(a ** b)
            else:
                return "ERR: SYNTAX"
                
    # At the end, exactly one result should remain in the stack
    if stack.size() != 1:
        return "ERR: SYNTAX"
        
    return stack.pop()

user_input = input("Enter Postfix expression (space-separated) : ")
result = evaluate_advanced_postfix(user_input)
print(f"Evaluated Result : {result}")
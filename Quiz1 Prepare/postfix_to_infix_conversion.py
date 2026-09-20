def postfix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    for char in expression:
        if char.isalnum():
            # Operands are just pushed to the stack
            stack.append(char)
        elif char in operators:
            # If there aren't two operands, it's a malformed expression
            if len(stack) < 2:
                return "Invalid Postfix Expression"
                
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Combine them with the operator and wrap in parentheses
            new_expr = f"({operand1}{char}{operand2})"
            stack.append(new_expr)
            
    if len(stack) == 1:
        return stack.pop()
    return "Invalid Postfix Expression"

user_input = input("Enter Postfix : ")
result = postfix_to_infix(user_input)
print(f"Infix : {result}")
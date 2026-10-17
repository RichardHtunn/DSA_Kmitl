def prefix_to_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    
    # Reverse the string to process it from right to left
    reversed_expr = expression[::-1]
    
    for char in reversed_expr:
        if char.isalnum():
            stack.append(char)
        elif char in operators:
            if len(stack) < 2:
                return "Invalid Prefix Expression"
                
            # Because we reversed the string, the first popped is operand1
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            # Combine in postfix format: Op1 Op2 Operator
            new_expr = f"{operand1}{operand2}{char}"
            stack.append(new_expr)
            
    if len(stack) == 1:
        return stack.pop()
    return "Invalid Prefix Expression"

user_input = input("Enter Prefix : ")
result = prefix_to_postfix(user_input)
print(f"Postfix : {result}")
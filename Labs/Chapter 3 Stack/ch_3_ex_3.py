def infix_to_postfix(experssion):
    operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    stack = []
    postfix = []

    for char in experssion:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and operator_priority[stack[-1]] >= operator_priority[char]):
                postfix.append(stack.pop())

            stack.append(char)
            
    while stack:
        postfix.append(stack.pop())
        
    return "".join(postfix)

user_input = input("Enter Infix : ")
result = infix_to_postfix(user_input)
print(f"Postfix : {result}")
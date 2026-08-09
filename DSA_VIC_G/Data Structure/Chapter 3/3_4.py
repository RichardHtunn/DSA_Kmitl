print("* Stack Calculator *")
User_input = input("Enter arguments : ").split(" ")
stack = []
error = False

for i in User_input:
    if i.isdigit():
        stack.append(int(i))
    elif i == "+":
        v1 = stack.pop()
        v2 = stack.pop()
        stack.append(v1 + v2)
    elif i == "-":
        v1 = stack.pop()
        v2 = stack.pop()
        stack.append(v1 - v2)
    elif i == "*":
        v1 = stack.pop()
        v2 = stack.pop()
        stack.append(v1 * v2)
    elif i == "/":
        v1 = stack.pop()
        v2 = stack.pop()
        stack.append(v1 / v2)
    elif i == "DUP":
        if len(stack) > 0:
            stack.append(stack[-1])
    elif i == "POP":
        if len(stack) > 0:
            stack.pop()
    else:
        print(f"Invalid instruction: {i}")
        error = True
        break

if error == False:
    if len(stack) == 0:
        print(0)
    else:
        print(int(stack[-1]))


    

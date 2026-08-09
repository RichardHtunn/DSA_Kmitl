User_input = input("Enter Infix : ")
postfix = ""
stack = []
operators = {"^" : 3, "*" : 2, "/" : 2, "+" : 1, "-" : 1}

for i in User_input:
    if i.isalpha():
        postfix += i
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while len(stack) > 0 and stack[-1] != "(":
            postfix += stack.pop()
        if len(stack) > 0:
            stack.pop()
    elif i in operators:
        while len(stack) > 0 and stack[-1] != "(" and operators[stack[-1]] >=  operators[i]:
            postfix += stack.pop()
        stack.append(i)

while len(stack) > 0:
    postfix += stack.pop()
print(f"Postfix : {postfix}")
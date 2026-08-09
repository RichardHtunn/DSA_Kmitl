User_input = input("Enter Input : ")
stack = []
need = 0
for i in User_input:
    if i == "(" or i == "[":
        stack.append(i)
    elif i == ")":
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            need += 1
    elif i == "]":
        if stack and stack[-1] == "[":
            stack.pop()
        else:
            need += 1

need += len(stack)
if need == 0:
    print(need)
    print("Perfect ! ! !")
else:
    print(need)
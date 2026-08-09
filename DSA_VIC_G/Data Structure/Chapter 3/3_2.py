User_input = input("Enter expresion : ")
stack = []
error = ""

for i in User_input:
    if i == "(" or i == "[" or i == "{":
        stack.append(i)
    elif i == ")":
        if len(stack) == 0:
            error = "close paren excess"
            break
        elif stack[-1] == "(":
            stack.pop()
        else:
            error = "Unmatch open-close"
            break
    elif i == "]":
        if len(stack) == 0:
            error = "close paren excess"
            break
        elif stack[-1] == "[":
            stack.pop()
        else:
            error = "Unmatch open-close"
            break
    elif i == "}":
        if len(stack) == 0:
            error = "close paren excess"
            break
        elif stack[-1] == "{":
            stack.pop()
        else:
            error = "Unmatch open-close"
            break

if error != "":
    print(f"{User_input} {error}")
elif len(stack) > 0:
    n = "".join(stack)
    print(f"{User_input} open paren excess   {len(stack)} : {n}")
else:
    print(f"{User_input} MATCH")



# open = []
# close = []
# need = 0
# match = 0
# for i in User_input:
#     if i == "(" or i == "[" or i == "{":
#         stack.append(i)
#         open.append(i)
#     elif i == ")":
#         close.append(i)
#         if stack and stack[-1] == "(":
#             stack.pop()
#             match += 1
#         else:
#             need += 1
#     elif i == "]":
#         close.append(i)
#         if stack and stack[-1] == "[":
#             stack.pop()
#             match += 1
#         else:
#             need += 1
#     elif i == "}":
#         close.append(i)
#         if stack and stack[-1] == "}":
#             stack.pop()
#             match += 1
#         else:
#             need += 1

# need += len(stack)
# if need == 0:
#     print(f"{User_input} MATCH")
# elif len(close) > len(open) and match > 0:
        
#         print(f"{User_input} close paren excess")
    
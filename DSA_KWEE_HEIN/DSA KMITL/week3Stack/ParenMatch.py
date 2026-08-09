# use stack to solve this 
# parenthese match
def match(open, close):
    return (open == '('and close ==')') or \
            (open == '{'and close =='}') or \
            (open == '['and close ==']')
            

def Parentheses(items):
    stack = []
    error = 0
    i = 0 # index to locate 

    # beginning
    while i < len(items) and error == 0:
        ch = items[i]
        # append the open to stack
        if ch in ['(','{' ,'[']:    
            # debugging line
            # print(ch)
            stack.append(ch)
            # print(stack)
        else:
            if ch in [')','}',']']:        
                # debugger
                # print(ch)
                if len(stack) > 0:
                                # top one on stack and ch
                    if not match(stack.pop(),ch):
                        error = 1
                        # print("Here Error 1")
                        # print(stack)
                else:
                    error = 2
        i += 1

    # Remaining opening brackets each need one closing bracket
    if len(stack) > 0 and error == 0:
        # debugging line, 
        # print(stack)
        error = 3
        # print("Here Error 3")
    return error, ch, i, stack

user_input = input("Enter expresion : ")

err, ch, i, stack = Parentheses(user_input)

if err == 1:
    print(user_input, 'Unmatch open-close')
elif err == 2:
    print(user_input, 'close paren excess')
elif err == 3:
    print(user_input, 'open paren excess  ', len(stack),': ',end='')
    for e in stack:
        print(e, sep=' ',end='')
    print()
else:
    print(user_input, 'MATCH')
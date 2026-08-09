# take the input as infix and swich to postfix

def toPostfix(items):
    # + - * / ^
    # order (, append, then level1 + -, 2 * /, right to left ^
    # empty stack to handle
    op_rank = {"+": 1,'-': 1, '*': 2, '/': 2, '^' : 3}
    stack = []
    answer = []
    for ch in items:
        # if open, then append instantly
           # is alnum, then append first
        if ch.isalnum():
            answer.append(ch)
        # handle the parentheses
        elif ch == '(':
            stack.append(ch)
        # handle the )
        elif ch == ')':
            # find the ( exist in stack or not, there may be other op on ( so
            # loop then all and pop it out
            while len(stack) > 0 and stack[-1] != '(': 
                # pop them and append to answer
                temp = stack.pop()
                answer.append(temp)
            # after op were gone, then () only left
            stack.pop()
        else:
            # handle the operators
            # the top shouldn't be open and compare the ones with dics
                while len(stack) > 0 and stack[-1] != '(' and op_rank[stack[-1]] >= op_rank[ch]: 
                    # here, if the ones already existed, then do comparison
                    temp = stack.pop()
                    answer.append(temp)
                stack.append(ch)
    while len(stack) > 0:
        # append the remaining ones
        temp = stack.pop()
        answer.append(temp) 
      
    return "".join(answer)

# userinput
user_input = input("Enter Infix : ")
answer = toPostfix(user_input)
print(f"Postfix : {answer}")
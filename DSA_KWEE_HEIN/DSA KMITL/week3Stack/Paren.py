def Parentheses(items):
    stack = []
    pairs = {')': '(', ']': '['}
    counter = 0

    for ch in items:
        if ch in ['(', '[']:         
            stack.append(ch)

        elif ch in [')', ']']:        # closing bracket
            if stack and stack[-1] == pairs[ch]:
                stack.pop()
            else:
                # Need one opening bracket
                counter += 1

    # Remaining opening brackets each need one closing bracket
    counter += len(stack)

    return counter


user_input = input("Enter Input : ")

needed = Parentheses(user_input)

if needed == 0:
    print('0')
    print("Perfect ! ! !")
else:
    print(needed)
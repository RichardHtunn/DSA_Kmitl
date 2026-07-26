def checking_bracket(text):
    stack = []
    missing_closing_brackets = 0

    for char in text:
        if char in "([":
            stack.append(char)

        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:   
                missing_closing_brackets += 1
            
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                missing_closing_brackets += 1

    total_missing = len(stack) + missing_closing_brackets

    print(total_missing)
    if total_missing == 0:
        print("Perfect ! ! !")

user_input = input("Enter Input : ")
checking_bracket(user_input)
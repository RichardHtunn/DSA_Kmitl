def check_expression(expression):
    stack = []
    
    open_brackets = "([{"
    close_brackets = ")]}"
    matches = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in open_brackets:
            stack.append(char)
            
        elif char in close_brackets:
            if not stack:
                print(f"{expression} close paren excess")
                return
            
            top = stack.pop()
            
            if matches[char] != top:
                print(f"{expression} Unmatch open-close")
                return
                
    if stack:
        excess_count = len(stack)
        excess_str = "".join(stack) 
        print(f"{expression} open paren excess   {excess_count} : {excess_str}")
        
    else:
        print(f"{expression} MATCH")

user_input = input("Enter expresion : ")
check_expression(user_input)
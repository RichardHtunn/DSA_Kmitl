# calculator
class Stack:
    # empty list as storage 
    def __init__(self):
        self.storage = []

    # push function
    def push(self, value):
        self.storage.append(value) 
    
    # pop function
    def pop(self):
        # check the length first
        if len(self.storage) == 0:
            return 0
        else:
            temp = self.storage[-1]
            del self.storage[-1]
            return temp 
    
    # peek the stack
    def peek(self):
        # check the len
        if len(self.storage) == 0:
            return 0
        else:
            temp = self.storage[-1]
            return temp

# now the function
# if the input not operators and num, not okay
def Calculator(items):
    # check the input valid or not
    s = Stack()
    n = len(items)
    i = 0
    while i < n:
        ch = items[i]
        # handle the int first
        if ch.lstrip('-').isdigit():
            s.push(int(ch))
        elif ch == '+':
            a = s.pop()
            b = s.pop()
            result = a + b
            s.push(result) 
        elif ch == '-':
            a = s.pop()
            b = s.pop()
            result = a - b
            s.push(result) 
        elif ch == '*':
            a = s.pop()
            b = s.pop()
            result = a * b
            s.push(result) 
        elif ch == '/':
            a = s.pop()
            b = s.pop()
            result = a / b
            s.push(int(result))
        elif ch == 'DUP':
            temp = s.peek()
            s.push(temp)
        elif ch == 'POP':
            s.pop()
        elif ch == "PSH":
            # check for the next item exists or not
            next = i + 1
            if next < n:
                temp = items[next]
                s.push(int(temp))
                i += 1

        else:
            return f"Invalid instruction: {ch}"
        i += 1

    # get the final value from the top of stack
    return s.peek()

print("* Stack Calculator *")
user_input = input("Enter arguments : ").split()
answer = Calculator(user_input)
print(answer)
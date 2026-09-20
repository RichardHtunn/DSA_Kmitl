class Calculator:
    def __init__(self):
        self.stack = []

    def run(self, instructions):
        tokens = instructions.split()
        i = 0
        
        while i < len(tokens):
            token = tokens[i]

            if token == '+':
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.append(b + a)
                
            elif token == '-':
                a = self.stack.pop()     
                b = self.stack.pop()     
                self.stack.append(a - b) 
                
            elif token == '*':
                a = self.stack.pop()    
                b = self.stack.pop()
                self.stack.append(b * a)
                
            elif token == '/':
                a = self.stack.pop()     
                b = self.stack.pop()     
                self.stack.append(int(a / b)) 

            elif token == 'DUP':
                self.stack.append(self.stack[-1])
                
            elif token == 'POP':
                self.stack.pop()
                
            elif token == 'PSH':
                i += 1
                if i < len(tokens):
                    self.stack.append(int(tokens[i]))

            elif token.lstrip('-').isdigit():
                self.stack.append(int(token))
                
            else:
                return f"Invalid instruction: {token}"
            
            i += 1

        if self.stack:
            return self.stack[-1]
        return 0

print("* Stack Calculator *")
user_input = input("Enter arguments : ")

calc = Calculator()
result = calc.run(user_input)
print(result)
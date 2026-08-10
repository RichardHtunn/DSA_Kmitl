class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        # self.size = len(self.items)

    def push(self, i):
        self.items.append(i)
        # self.size += 1

    def pop(self):
        # self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        # return self.items = []
        return len(self.items) == 0

    def isFull(self):
        pass

    def size(self):
        return len(self.items)

    def __str__(self):
        s = 'stack of '+str(self.size())+' items : '
        for i in self.items:
            s += str(i)+' '
        return s


inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

sec1 = ['+', '-']
sec2 = ['*', '/']
sec3 = ['^']

### Enter Your Code Here ###
for i in range(0, len(inp), 1):
    if inp[i] in sec1:
        if S.isEmpty():
            S.push(inp[i])
        else:
            while not S.isEmpty() and S.peek() != '(':
                print(S.pop(), end='')
                if S.isEmpty():
                    break 
            S.push(inp[i])
    elif inp[i] in sec2:
        if S.isEmpty() or S.peek() in sec1 or S.peek() == '(':
            S.push(inp[i])
        elif S.peek() in sec2 or S.peek() in sec3:
            print(S.pop(), end='')
            S.push(inp[i])
    elif inp[i] in sec3:
        S.push(inp[i])
    elif inp[i] == '(':
        S.push(inp[i])
    elif inp[i] == ')':
        while S.peek() != '(':
            print(S.pop(), end='')
        else:
            S.pop()
    else:
        print(inp[i], end='')

while not S.isEmpty():

    print(S.pop(), end='')

print()
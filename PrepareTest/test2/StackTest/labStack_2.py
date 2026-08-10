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


S = Stack()
open = ['{', '[', '(']
close = ['}', ']', ')']
check = {'}':'{', ']':'[', ')':'('}
stop = False
match = False

inp = input("Enter expresion : ")
print(inp, end=' ')

for i in inp:
    if i in open:
        S.push(i)
    elif i in close:
        if S.isEmpty():
            print("close paren excess")
            stop = True
            match = True
            break
        else:
            temp = S.pop()
            if check[i] == temp:
                pass
            else:
                print("Unmatch open-close")
                stop = True
                match = True
                break

if S.isEmpty() and match == False:
    print("MATCH")
elif stop == False:
    print("open paren excess ", S.size(), ":", end=' ')
    for i in S.items:
        print(i, end=' ')

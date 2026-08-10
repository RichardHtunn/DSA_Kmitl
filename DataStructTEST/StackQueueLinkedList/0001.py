class Stack:
    def __init__(self, list=None): # With Defualt Argument
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self, new_data):
        self.items.append(new_data)

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        return self.items.pop()

    def popFirst(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.items[-1]

    def bottom(self):
        if self.isEmpty():
            raise Exception("empty stack")
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return " ".join([str(x) for x in self.items])


inp = input("Enter choice : ")

s1 = Stack()
s2 = Stack()

if inp == '1':
    s1.push(10)
    s1.push(20)
    print("Data in Stack is : ", end='')
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack : ", end='')
    print(s1.peek())
    print("Bottom of stack : ", end='')
    print(s1.bottom())
elif inp == '2':
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print("Data in Stack is : ", end='')
    print(s1)
    print("Stack is Empty : ", end='')
    print(s1.isEmpty())
elif inp == '3':
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print("Data in Stack is : ", end='')
    print(s1)
    print("Stack size :",s1.size())
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

print("Enter Input :", end=' ')
text = input().split(",")

for i in range(0, len(text), 1):
    if text[i][0] == 'A':
        temp = int(text[i][2:])
        S.push(temp)
        print("Add =", temp, "Size =", S.size())
    elif text[i][0] == 'P':
        if S.isEmpty():
            print("-1")
        else:
            index = S.size()-1
            print("Pop =", S.pop(), "and Index =", index)

if S.isEmpty():
    print("Value in Stack = Empty")
else:
    print("Value in Stack =", end=' ')
    for i in S.items:
        print(i, end=' ')
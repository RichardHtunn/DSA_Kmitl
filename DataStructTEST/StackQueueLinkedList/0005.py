class QueueList:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, new_Data):
        self.items.append(new_Data)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        pass

    def size(self):
        return len(self.items)

    def front(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[0]

    def tail(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[-1]


inp = input("Enter Input : ").split('/')
# print(inp)

# print(inp[0].split())

# print(inp[1].split(','))

temp = inp[0].split()

temp2 = inp[1].split(',')
# print(temp2)
# print(temp2[0])

# print("")

q = QueueList(temp)
# print(q.items)

for i in range(0, len(temp2), 1):
    if temp2[i][0] == 'E':
        q.enQueue(temp2[i][2:])
    elif temp2[i][0] == 'D':
        q.deQueue()

# print(q.items)

check = []
x = True

for i in q.items:
    if i not in check:
        check.append(i)
    else:
        x = False
        break

if x == True:
    print("NO Duplicate")
else:
    print("Duplicate")
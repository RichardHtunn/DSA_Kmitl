from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enQueue(self, new_data):
        self.items.append(new_data)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0

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


q = Queue()

inp = input("Enter Input : ").split(',')

for i in range(0, len(inp), 1):
    if inp[i][0] == 'E':
        q.enQueue(int(inp[i][2:]))
        print("Add", inp[i][2:], "index is", q.size()-1)
    elif inp[i][0] == 'D':
        if q.isEmpty():
            print("-1")
        else:
            temp = q.deQueue()
            print("Pop", temp, "size in queue is", q.size())

# print(q)
# print(q.size())
# print(q.isEmpty())

if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is :  [", end='')
    for i in range(0, q.size(), 1):
        if i == q.size()-1:
            print("'"+str(q.items[i])+"']")
        else:
            print("'"+str(q.items[i])+"', ", end='')

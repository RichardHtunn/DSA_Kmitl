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

    def printWithOut(self):
        if len(self.items) == 0:
            print("[]", end=' ')
        else:
            print('[', end='')
            for i in range(0, len(self.items), 1):
                print("'", end='')
                print(self.items[i], end='')
                print("'", end='')
                if i == len(self.items)-1:
                    print("]", end=' ')
                else:
                    print(",", end=' ')


q = Queue()
cash1 = Queue()
cash2 = Queue()

inp = input("Enter people : ")

for i in inp:
    q.enQueue(i)

round = 1
while not q.isEmpty():
    
    print(round, end=' ')

    if cash1.size() == 5:
        temp = q.deQueue()
        cash2.enQueue(temp)
    else:
        temp = q.deQueue()
        cash1.enQueue(temp)

    # show
    q.printWithOut()
    cash1.printWithOut()
    cash2.printWithOut()
    print("")

    round = round+1

    if (round-1)%3 == 0:
        cash1.deQueue()
    
    if round%2 == 0 and not cash2.isEmpty():
        cash2.deQueue()
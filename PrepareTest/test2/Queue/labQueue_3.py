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


# print(chr(103))
# print(ord('g'))

q = Queue()

inp = input("Enter code,hint : ")

diff = ord(inp[-1])-ord(inp[0])

for i in inp:
    if i == ',':
        break
    else:
        temp = ord(i) + diff
        temp = chr(temp)
        q.enQueue(temp)
        q.printWithOut()
        print("")
        
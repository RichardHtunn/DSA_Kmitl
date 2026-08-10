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

    def __str__(self):
        return " ".join(str(x) for x in self.items)


inp = input("Enter choice : ")

if inp == '1':
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print("Queue data : ", end='')
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :", q1.size())
    print("Queue data : ", end='')
    print(q1)
elif inp == '2':
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print("Queue data : ", end='')
    print(q1)
    print("Queue is Empty :",q1.isEmpty())
elif inp == '3':
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    if q1.size() == 0:
        print("Empty Queue")
    else:
        print("Queue data : ", end='')
        print(q1)
    print("Size of Queue :", q1.size())
    print("Queue is Empty :",q1.isEmpty())

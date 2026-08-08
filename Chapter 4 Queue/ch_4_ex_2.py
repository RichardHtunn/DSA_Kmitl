class Queue:
    def __init__(self, firstList = None):
        if firstList is None:
            self.items = []
        else:
            self.items = list(firstList)

    def enQueue(self, item):
        self.items.append(item)
    
    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

user_input = input("Enter people : ")

mainQueue = Queue(user_input)
c1Queue = Queue()
c2Queue = Queue()

c1Timer = 0
c2Timer = 0
time = 1

while not mainQueue.isEmpty():
    if not c1Queue.isEmpty():
        c1Timer += 1
        if c1Timer == 3:
            c1Queue.deQueue()
            c1Timer = 0

    if not c2Queue.isEmpty():
        c2Timer += 1
        if c2Timer == 2:
            c2Queue.deQueue()
            c2Timer = 0
        
    person = mainQueue.deQueue()

    if c1Queue.size() < 5:
        c1Queue.enQueue(person)
    elif c2Queue.size() < 5:
        c2Queue.enQueue(person)

    print(f"{time} {mainQueue.items} {c1Queue.items} {c2Queue.items}")
    time += 1
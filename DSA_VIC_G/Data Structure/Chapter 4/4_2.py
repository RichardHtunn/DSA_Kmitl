class Queue:
    def __init__(self, main_list = None):
        if main_list is None:
            self.items = []
        else:
            self.items = list(main_list)    
    def enQueue(self, i):
        self.items.append(i)
    def deQueue(self):
        if not self.IsEmpty():
            return self.items.pop(0)
    def IsEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)  

User_input = input("Enter people : ")
main = Queue(User_input)
List1 = Queue()
List2 = Queue()
time1 = 0
time2 = 0
num = 1

while not main.IsEmpty():
    if not List1.IsEmpty():
        time1 += 1
        if time1 == 3:
            List1.deQueue()
            time1 = 0
    if not List2.IsEmpty():
        time2 += 1
        if time2 == 2:
            List2.deQueue()
            time2 = 0
    
    letter = main.deQueue()
    if List1.size() < 5:
        List1.enQueue(letter)
    elif List2.size() < 5:
        List2.enQueue(letter)

    print(f"{num} {main.items} {List1.items} {List2.items}")
    num += 1
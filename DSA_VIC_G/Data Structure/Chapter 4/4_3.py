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

User_input = input("input : ").split(",")
q = Queue(User_input)
num_queue = Queue()
error_dequeue = 0
error_input = 0
enqueue = 0

while not q.IsEmpty():
    place = q.deQueue()
    letter = place[0]
    number_part = place[1:] 
    print(f"Step : {place}")
    
    if letter == 'E':
        number = int(number_part)
        for i in range(number):
            num_queue.enQueue(f"*{enqueue}")
            enqueue += 1
        print(f"Enqueue : {num_queue.items}")
        
    elif letter == 'D' and number_part.isdigit():
        number = int(number_part)
        for i in range(number):
            if not num_queue.IsEmpty():
                num_queue.deQueue()
            else:
                error_dequeue += 1
        print(f"Dequeue : {num_queue.items}")
        
    else:
        error_input += 1
        print(num_queue.items)
        
    print(f"Error Dequeue : {error_dequeue}")
    print(f"Error input : {error_input}")
    print("--------------------")
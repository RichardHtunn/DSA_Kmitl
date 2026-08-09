# class Queue:
#     def __init__(self):
#         self.items = []

#     def enQueue(self, item):
#         self.items.append(item)

#     def deQueue(self):
#         if not self.isEmpty():
#             return self.items.pop(0)

#     def isEmpty(self):
#         return len(self.items) == 0
    
#     def size(self):
#         return len(self.items)
    
# user_input = input("input : ")

# items = [x.strip() for x in user_input.split(',')]

# q = Queue()
# errorDequeue = 0
# errorInput = 0
# enQueueCounter = 0

# for item in items:
#     print(f"Step : {item}")

#     if len(item) > 1 and item[0] in ('E', 'D') and item[1:].isdigit():
#         op = item[0]
#         count = int(item[1:])

#         if op == 'E':
#             for _ in range(count):
#                 q.enQueue(f"*{enQueueCounter}")
#                 enQueueCounter += 1
#             print(f"Enqueue : {q.items}")
#             print(f"Error Dequeue : {errorDequeue}")
#             print(f"Error input : {errorInput}")
#             print("--------------------")
#         elif op == 'D':
#             for _ in range(count):
#                 if not q.isEmpty():
#                     q.deQueue()
#                 else:
#                     errorDequeue += 1
#             print(f"Dequeue : {q.items}")
#             print(f"Error Dequeue : {errorDequeue}")
#             print(f"Error input : {errorInput}")
#             print("--------------------")
#     else:
#         errorInput += 1
#         print(f"{q.items}")
#         print(f"Error Dequeue : {errorDequeue}")
#         print(f"Error input : {errorInput}")
#         print("--------------------")



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
print(f"NUM que {num_queue.items}")
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
        
    elif letter == 'D':
        number = int(number_part)
        for i in range(number):
            if not num_queue.IsEmpty():
                num_queue.deQueue()
            else:
                error_dequeue += 1
        print(f"Dequeue : {num_queue.items}")
        
    else:
        error_input += 1
        print(f"Queue : {num_queue.items}")
        
    print(f"Error Dequeue : {error_dequeue}")
    print(f"Error input : {error_input}")
    print("--------------------")
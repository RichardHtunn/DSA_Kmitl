class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
user_input = input("input : ")

items = [x.strip() for x in user_input.split(',')]

q = Queue()
errorDequeue = 0
errorInput = 0
enQueueCounter = 0

for item in items:
    print(f"Step : {item}")

    if len(item) > 1 and item[0] in ('E', 'D') and item[1:].isdigit():
        op = item[0]
        count = int(item[1:])

        if op == 'E':
            for _ in range(count):
                q.enQueue(f"*{enQueueCounter}")
                enQueueCounter += 1
            print(f"Enqueue : {q.items}")
            print(f"Error Dequeue : {errorDequeue}")
            print(f"Error input : {errorInput}")
            print("--------------------")
        elif op == 'D':
            for _ in range(count):
                if not q.isEmpty():
                    q.deQueue()
                else:
                    errorDequeue += 1
            print(f"Dequeue : {q.items}")
            print(f"Error Dequeue : {errorDequeue}")
            print(f"Error input : {errorInput}")
            print("--------------------")
    else:
        errorInput += 1
        print(f"{q.items}")
        print(f"Error Dequeue : {errorDequeue}")
        print(f"Error input : {errorInput}")
        print("--------------------")
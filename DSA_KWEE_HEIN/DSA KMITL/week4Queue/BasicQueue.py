class Queue:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
       return str(self.items)
    
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []
       # return len(self.items) == 0

    def size(self):
        return len(self.items)

# regular queue
def RegularQ(input):
    queue = Queue()
    # seperate using space
    for a in input:
        parts = a.strip().split(" ",1)
        op = parts[0]
        # debugger
        # print(op)
        num = parts[1] if len(parts) > 1 else None
        # debugger
        # print(num)
        # do the process
        if op == "E" and num is not None:
            # debugger
            # print("Here working")
            queue.enQueue(num)
            print(f"Add {num} index is {queue.size()- 1}")
            # debugger
            # print(queue)
        elif op == 'D' and num == None:
            if not queue.isEmpty():
                print(f"Pop {int(queue.items[0])} size in queue is {queue.size()-1}")
                pop_value = queue.deQueue()

            else:
                print("-1")
    if queue.isEmpty():
        print("Empty")

    return queue


user_input = input("Enter Input : ").split(",")
# debugger
# print(user_input)
answer = RegularQ(user_input)
if not answer.isEmpty():
    print(f"Number in Queue is :  {answer}")
else:
    None
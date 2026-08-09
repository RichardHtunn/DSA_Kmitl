# two dimension
# normal q class now
user_input = input("Enter Input (Normal, Mirror) : ").split(" ")
d2input = user_input[0]
d3input = user_input[1]

class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items =[]
        else:
            self.items = list
    
    def __str__(self):
        return str([f"*{x}" for x in self.items])
    
    def enQueue(self,i ):
        self.items.append(i)
    
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

class Stack:
    # empty list as storage 
    def __init__(self):
        self.storage = []
    def __str__(self):
        return "".join(reversed(self.storage))

    # push function
    def push(self, value):
        self.storage.append(value) 
    
    # pop function
    def pop(self):
        # check the length first
        if len(self.storage) == 0:
            return 0
        else:
            temp = self.storage[-1]
            del self.storage[-1]
            return temp 
    def size(self):
        return len(self.storage)

    # peek the stack
    def peek(self):
        # check the len
        if len(self.storage) == 0:
            return 0
        else:
            temp = self.storage[-1]
            return temp
def mirror(d2input):
    mirrorStack = Stack()
    itemqueue = Queue()
    mirrorE = 0
    # first put all d2 input into stack with reversed
    reversed_data = d2input[::-1]
    for ch in reversed_data:
        # if two already exists and third one the same
        if (mirrorStack.size() >= 2 and mirrorStack.storage[-2] == ch and mirrorStack.storage[-1] == ch):
            mirrorStack.pop()
            mirrorStack.pop()

            itemqueue.enQueue(ch)
            mirrorE += 1
        else:
            mirrorStack.push(ch)
    return mirrorStack, itemqueue, mirrorE

def real(d1input, itemqueue):
    realStack = Stack()
    realE = 0
    failed = 0
    for ch in d1input:
        if realStack.size() < 2:
            realStack.push(ch)
        else:
            top1 = realStack.storage[-2]
            top2 = realStack.storage[-1]

            # let's check if the three are same without interception first
            if top1 == ch and top2 == ch:
                # let's check there will be interception from mirror q
                if not itemqueue.isEmpty():
                    block = itemqueue.dequeue()

                    if block != ch:
                        realStack.push(block)
                        realStack.push(ch)
                    else:
                        realStack.push(block)
                        realStack.pop()
                        realStack.pop()
                        # realE += 1
                        failed += 1
                # no item in mirror q and normal explosion happens
                else:
                    realStack.pop()
                    realStack.pop()
                    realE += 1
            else:
                realStack.push(ch)
    return realStack, realE, failed

def display(realStack, realE, failed, mirrorStack, mirrorE):
    # Determine stack display values
    real_content = realStack if realStack.size() > 0 else "Empty"
    mirror_content = mirrorStack if mirrorStack.size() > 0 else "ytpmE"

    # Print Normal section
    print("NORMAL :")
    print(realStack.size())
    print(real_content)
    print(realE, "Explosive(s) ! ! ! (NORMAL)")

    # Print failed status if present
    if failed:
        print("Failed Interrupted", failed, "Bomb(s)")

    # Print Mirror section
    print("------------MIRROR------------")
    print(": RORRIM")
    print(mirrorStack.size())
    print(mirror_content)
    print("(RORRIM) ! ! ! (s)evisolpxE", mirrorE)
        
mirrorStack, itemqueue, mirrorE = mirror(d3input)
realStack, realE, failed = real(d2input, itemqueue)

display(realStack, realE, failed, mirrorStack, mirrorE)
